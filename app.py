from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
async def sample_api():
    return {"message": "hello world"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


