<div class="termy">

```console
$ fastapi dev main.py

 ╭────────── FastAPI CLI - Development mode ───────────╮
 │                                                     │
 │  Serving at: http://127.0.0.1:8000                  │
 │                                                     │
 │  API docs: http://127.0.0.1:8000/docs               │
 │                                                     │
 │  Running in development mode, for production use:   │
 │                                                     │
 │  fastapi run                                        │
 │                                                     │
 ╰─────────────────────────────────────────────────────╯

INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2248755] using WatchFiles
INFO:     Started server process [2248757]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>


[//]: # (```Python hl_lines="4  9-12  25-27")

[//]: # (from typing import Union)

[//]: # ()

[//]: # (from fastapi import FastAPI)

[//]: # (from pydantic import BaseModel)

[//]: # ()

[//]: # (app = FastAPI&#40;&#41;)

[//]: # ()

[//]: # ()

[//]: # (class Item&#40;BaseModel&#41;:)

[//]: # (    name: str)

[//]: # (    price: float)

[//]: # (    is_offer: Union[bool, None] = None)

[//]: # ()

[//]: # ()

[//]: # (@app.get&#40;"/"&#41;)

[//]: # (def read_root&#40;&#41;:)

[//]: # (    return {"Hello": "World"})

[//]: # ()

[//]: # ()

[//]: # (@app.get&#40;"/items/{item_id}"&#41;)

[//]: # (def read_item&#40;item_id: int, q: Union[str, None] = None&#41;:)

[//]: # (    return {"item_id": item_id, "q": q})

[//]: # ()

[//]: # ()

[//]: # (@app.put&#40;"/items/{item_id}"&#41;)

[//]: # (def update_item&#40;item_id: int, item: Item&#41;:)

[//]: # (    return {"item_name": item.name, "item_id": item_id})

[//]: # (```)

## `fastapi-slim`

If you don't want the extra standard optional dependencies, install `fastapi-slim` instead.

When you install with:

```bash
pip install fastapi
```

...it includes the same code and dependencies as:

```bash
pip install "fastapi-slim[standard]"
```

## `Application structure`

```console
    .
    └── app/
        ├── backend/            # Backend functionality and configs
        |   ├── config.py           # Configuration settings
        │   └── session.py          # Database session manager
        ├── models/             # SQLAlchemy models
        │   ├── auth.py             # Authentication models
        |   ├── base.py             # Base classes, mixins
        |   └── ...                 # Other service models
        ├── routers/            # API routes
        |   ├── auth.py             # Authentication routers
        │   └── ...                 # Other service routers
        ├── schemas/            # Pydantic models
        |   ├── auth.py              
        │   └── ...
        ├── services/           # Business logic
        |   ├── auth.py             # Generate and verify tokens
        |   ├── base.py             # Base classes, mixins
        │   └── ...
        ├── cli.py              # Command-line utilities
        ├── const.py            # Constants
        ├── exc.py              # Exception handlers
        └── main.py             # Application runner
```
    
