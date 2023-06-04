from typing import Union
from fastapi import FastAPI
from api.sixt import compare_results

app = FastAPI()

# API endpoint
@app.get("/")
def read_root():
  return "Welcome to Beluga API"

@app.get("/rent/vehicles/sixt/bulk/{num_days}")
def read_item(num_days: int = 3):
    return compare_results(num_days)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": "You called items number " + str(item_id) + " with query " + str(q)}