from typing import Union
from fastapi import FastAPI

# Importing the function that will be called when the API is called
from src.sixt import get_bulk_results

app = FastAPI()

# API endpoint
@app.get("/")
def read_root():
  return "Welcome to Beluga API 🐋 !"

@app.get("/rent/vehicles/sixt/bulk/{num_days}")
async def read_item(num_days: int = 3):
    return await get_bulk_results(num_days)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, " atq": "You called items number " + str(item_id) + " with query " + str(q)}