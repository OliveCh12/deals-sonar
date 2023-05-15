from typing import Union
from fastapi import FastAPI

from api.sixt import generate_url_yearly

app = FastAPI()

# API endpoint
@app.get("/")
def read_root():
  return "ok"



# @app.get("/rent/vehicles/sixt/bulk/{num_days}")
# def read_item(num_days: int = 3):
#     return generate_url_yearly(num_days)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": "On c'est pas trop ce que c'est"}