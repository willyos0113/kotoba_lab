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
| Agent 框架 | Claude AI Agent SDK |
| 容器化 | Docker + Docker Compose |
| 溝通方式 | REST API |

## 目前狀態

進行中的開發階段：
- ✅ 前後端基礎框架建立
- ✅ Docker Compose 容器化設置
- ✅ 簡單的 Agent 端點（Greeter Agent）
- ✅ Pydantic 模型定義
- ⏳ 日文音聲練習流程功能開發中

## 專案結構

```
kotoba_lab/
├── backend/                     # FastAPI 後端
│   ├── app/
│   │   ├── main.py              # 應用程式入口、路由定義
│   │   ├── agents/              # Agent 邏輯模組
│   │   │   └── greeter.py       # 問候 Agent（示例）
│   │   ├── schemas/             # Pydantic 請求/回應模型
│   │   │   └── schemas.py       # 資料結構定義
│   │   ├── models/              # 資料庫 ORM 模型（待開發）
│   │   ├── services/            # 商業邏輯層（待開發）
│   │   └── core/config.py       # 設定（讀取 .env）
│   ├── tests/                   # pytest 測試
│   ├── Dockerfile               # 後端容器定義
│   ├── requirements.txt
│   └── .env.example
├── frontend/                    # React 前端
│   ├── src/
│   │   ├── main.tsx             # 入口
│   │   ├── App.tsx
│   │   └── api/client.ts        # 呼叫後端 API 的封裝
│   ├── index.html
│   ├── vite.config.ts           # 含開發時 proxy 設定
│   ├── package.json
│   └── .env.example
├── compose.yaml                 # Docker Compose 編排文件
├── .gitignore
└── README.md
```

## 快速開始

### 環境需求

- **使用 Docker**：Docker 和 Docker Compose
- **本地開發**：Python 3.11+、Node.js 20+

### 方式 A：使用 Docker Compose（推薦）

```bash
docker-compose up --build
# 後端：http://localhost:8000
# 前端：http://localhost:5173（待容器化）
```

後端 API 文件：http://localhost:8000/docs

### 方式 B：本地開發環境

#### 啟動後端

```bash
cd backend
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload   # http://localhost:8000
```

#### 啟動前端

```bash
cd frontend
npm install
npm run dev                      # http://localhost:5173
```

### API 端點

| 方法 | 端點 | 說明 |
| --- | --- | --- |
| GET | `/` | 根路徑（返回 "Hello, World!"） |
| GET | `/{name}` | 簡單問候（路徑參數） |
| POST | `/greet` | 使用 Agent 生成客製化問候 |
| POST | `/items` | 建立項目（示例） |

API 互動文件：http://localhost:8000/docs（Swagger UI）

## 開發慣例

- 後端 Agent 邏輯放在 `app/agents/` 目錄下
- Pydantic 資料模型放在 `app/schemas/` 目錄下
- 機密與環境設定放 `.env`（已被 git 忽略），並同步更新 `.env.example`
- 前端呼叫後端統一經過 `src/api/client.ts`
- 破壞性 API 變更時規劃版本化策略（`/api/v2` 等）
