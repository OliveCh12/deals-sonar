from typing import Union
from fastapi import FastAPI

app = FastAPI()

# API endpoint
@app.get("/")
def read_root():
  return "ok"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": "On c'est pas trop ce que c'est"}