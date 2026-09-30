from fastapi import FastAPI, HTTPException
from app.agents.greeter import generate_greeting
from app.schemas.schemas import Item, GreetingRequest

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


@app.post("/greet")
async def greet(request: GreetingRequest):
    """
    呼叫問候 Agent，根據提供的名字回傳客製化問候語。
    """
    try:
        # 1. 感知環境：接收到請求中的名字
        user_name = request.name

        # 2. 決策與行動：根據名字生成問候語
        greeting_message = generate_greeting(user_name)

        # 3. 目標導向：回傳問候語以完成「問候」的目標
        return {"greeting": greeting_message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"發生錯誤：{e}")


@app.post("/items")
async def create_item(request: Item):
    """
    這個 API 接收一個 Item 物件 (包含 name, price, is_offer)，
    並回傳接收到的 Item 資料。
    """
    return request
