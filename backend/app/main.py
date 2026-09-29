from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root():
    """
     這是一個簡單的根路徑 API，回傳 "Hello World" 訊息。
    """
    return {"message": "Hello, World!"}

@app.get("/{name}")
async def greet_name(name: str):
    """
    這個 API 接收一個名字作為路徑參數，並回傳問候語。
    """
    return {"message": f"Hello {name}"}

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool

@app.post("/items")
async def create_item(request: Item):
    """
    這個 API 接收一個 Item 物件 (包含 name, price, is_offer)，
    並回傳接收到的 Item 資料。
    """
    return request
