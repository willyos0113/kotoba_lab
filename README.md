# Kotoba Lab

日文口說練習平台，協助已具備日文基礎、但口說輸出不足的台灣學習者，建立可持續的練習循環。

## 專案目標

許多台灣學習者已有一定的日文基礎，卻缺少開口說的機會與即時回饋。Kotoba Lab 讓使用者用固定的流程反覆練習：

1. **播放示範音檔**：聆聽標準發音
2. **錄音**：聽完後跟著說一次
3. **AI 自動評測**：系統分析錄音並給出評分與回饋
4. **查看結果**：檢視評測內容，作為下一輪練習的依據

## 技術架構

| 層級 | 技術 |
| --- | --- |
| 前端 | React + Vite + TypeScript |
| 後端 | FastAPI (Python) |
| 溝通方式 | REST API（`/api/v1`） |

## 目前狀態

專案骨架階段：前後端可以啟動，並以健康檢查 API 確認串接正常。練習流程的功能尚待開發。

## 專案結構

```
kotoba_lab/
├── backend/                 # FastAPI 後端
│   ├── app/
│   │   ├── main.py          # 應用程式入口（建立 app、CORS、掛載 router）
│   │   ├── api/v1/          # API 路由（版本化）
│   │   │   ├── router.py    # 彙整所有 endpoints
│   │   │   └── endpoints/   # 各功能的路由檔（health.py ...）
│   │   ├── core/config.py   # 設定（讀取 .env）
│   │   ├── schemas/         # Pydantic 請求/回應模型（之後新增）
│   │   ├── models/          # 資料庫 ORM 模型（之後新增）
│   │   └── services/        # 商業邏輯（之後新增）
│   ├── tests/               # pytest 測試
│   ├── requirements.txt
│   └── .env.example
├── frontend/                # React 前端
│   ├── src/
│   │   ├── main.tsx         # 入口
│   │   ├── App.tsx
│   │   └── api/client.ts    # 呼叫後端 API 的封裝
│   ├── index.html
│   ├── vite.config.ts       # 含 /api → localhost:8000 的 proxy
│   ├── package.json
│   └── .env.example
├── .gitignore
└── README.md
```

> `schemas/`、`models/`、`services/` 等目錄在需要時再建立，避免空殼資料夾。

## 快速開始

### 環境需求

- Python 3.11+
- Node.js 20+

### 啟動後端

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env            # Windows PowerShell: Copy-Item .env.example .env
uvicorn app.main:app --reload   # http://localhost:8000
```

- API 文件：http://localhost:8000/docs
- 健康檢查：http://localhost:8000/api/v1/health
- 執行測試：`pytest`

### 啟動前端

```bash
cd frontend
npm install
npm run dev                     # http://localhost:5173
```

開發時前端透過 Vite proxy 將 `/api` 轉發到後端，請同時啟動兩邊。

## 開發慣例

- API 一律放在 `/api/v1` 之下，破壞性變更再開 `v2`。
- 機密與環境設定放 `.env`（已被 git 忽略），並同步更新 `.env.example`。
- 前端呼叫後端統一經過 `src/api/client.ts`。
