import os
import httpx
from pathlib import Path
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from app.tools.params_getter import _get_first_param

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

app = FastAPI(
    title="天氣 agent API",
    description="這是一個使用 FastAPI 建立的天氣 agent API，提供天氣相關的功能。"
)


@app.post("/weather")
async def get_weather(city: str) -> dict:
    """
    從中央氣象局 API 獲取指定城市的 36 小時天氣資訊
    """
    api_key = os.getenv("CWA_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="缺少 CWA_API_KEY 環境變數")

    if not city or not city.strip():
        raise HTTPException(status_code=400, detail="城市名稱不能為空")

    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"
    params = {
        "Authorization": api_key,
        "locationName": city,
        "format": "JSON"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=502, detail=f"API 請求失敗：{str(e)}")

    try:
        locations = data.get("records", {}).get("location", [])
        if not locations:
            raise HTTPException(status_code=404, detail="API 未返回位置資料")

        for loc in locations:
            if loc.get("locationName") == city:
                wx = _get_first_param(loc, "Wx")
                pop = _get_first_param(loc, "PoP")
                min_t = _get_first_param(loc, "MinT")
                max_t = _get_first_param(loc, "MaxT")
                ci = _get_first_param(loc, "CI")
                return {
                    "status": "success",
                    "city": city,
                    "report": (
                        f"{city} 天氣預報：{wx}，降雨機率 {pop}%，"
                        f"氣溫 {min_t}°C ~ {max_t}°C，體感 {ci}。"
                    )
                }
        raise HTTPException(status_code=404, detail=f"找不到 {city} 的天氣資料")
    except KeyError as e:
        raise HTTPException(status_code=502, detail=f"API 回應格式異常：{str(e)}")
