import asyncio
import random
import string
import time
import uuid

from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement, BatchStatement
from fastapi import FastAPI
from fastapi import Request
from pydantic import BaseModel

def string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(process_time)
    return response


# Connect to the Cassandra cluster
cluster = Cluster(['cassandra'], port=9042)
session = cluster.connect()


# Create keyspace and table if they do not exist
session.execute("""
CREATE KEYSPACE IF NOT EXISTS mykeyspace
WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 1}
""")
session.execute("""
CREATE TABLE IF NOT EXISTS mykeyspace.users (
    id UUID PRIMARY KEY,
    name TEXT
)
""")
session.set_keyspace('mykeyspace')


class User(BaseModel):
    name: str


@app.post("/users/")
async def create_user(user: User):
    batch = BatchStatement()

    for user in range(1_000):
        user_id = uuid.uuid4()
        user_name = string_generator(6)
        batch.add(SimpleStatement("INSERT INTO users (id, name) VALUES (%s, %s)"), (user_id, user_name))
    # batch.add(SimpleStatement("DELETE FROM pending_users WHERE name=%s"), (name,))
        session.execute_async(batch)

    # insert_user = session.prepare("INSERT INTO mykeyspace.users (id, name) VALUES (?, ?)")
    # batch = BatchStatement(consistency_level=ConsistencyLevel.QUORUM)
    # batch.add(insert_user, (user_id, user.name))
    # # query = SimpleStatement(
    # #     "INSERT INTO mykeyspace.users (id, name) VALUES (%s, %s)",
    # #     (user_id, user.name)
    # # )
    # session.execute(batch)
    return {
        'status': 'ok',
    }


@app.get("/users/")
def read_users():
    query = SimpleStatement("SELECT * FROM users")
    count = SimpleStatement("SELECT count(*) FROM users")
    rows = session.execute(count)
    return rows.one()
    # return [{"id": str(row.id), "name": row.name} for row in rows]


@app.get("/")
async def root():
    return {"Hello": "World"}
