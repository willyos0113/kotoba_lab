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
- ✅ 前後端基礎框架建立（React 19 + FastAPI）
- ✅ Docker Compose 後端容器化
- ✅ 模塊化工具函數設計（tools 目錄）
- ✅ Pydantic 資料模型定義
- ✅ 天氣 API 端點範例實現
- ⏳ 前端容器化設置
- ⏳ 日文音聲練習流程功能開發中

## 專案結構

```
kotoba_lab/
├── backend/                     # FastAPI 後端
│   ├── app/
│   │   ├── main.py              # 應用程式入口、路由定義
│   │   ├── tools/               # 工具函數與邏輯模組
│   │   │   ├── greeter.py       # 問候工具函數
│   │   │   └── params_getter.py # 參數提取工具
│   │   ├── models/              # Pydantic 資料模型
│   │   │   └── models.py        # 資料結構定義（Item, GreetingRequest 等）
│   │   └── services/            # 商業邏輯層（待開發）
│   ├── tests/                   # pytest 測試
│   ├── Dockerfile               # 後端容器定義
│   ├── requirements.txt         # Python 依賴
│   ├── pytest.ini               # pytest 配置
│   └── .env.example
├── frontend/                    # React 前端
│   ├── src/
│   │   ├── main.tsx             # 應用入口
│   │   ├── App.tsx              # 主頁面組件
│   │   └── api/client.ts        # 後端 API 呼叫封裝
│   ├── index.html
│   ├── vite.config.ts           # Vite 構建配置
│   ├── tsconfig.json            # TypeScript 配置
│   ├── package.json
│   ├── package-lock.json
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
| POST | `/weather` | 獲取指定城市的天氣預報（需要 CWA_API_KEY） |

**請求範例：**
```bash
curl -X POST "http://localhost:8000/weather?city=台北" \
  -H "Content-Type: application/json"
```

**回應範例：**
```json
{
  "status": "success",
  "city": "台北",
  "report": "台北 天氣預報：陰，降雨機率 30%，氣溫 18°C ~ 24°C，體感舒適。"
}
```

API 互動文件：http://localhost:8000/docs（Swagger UI）

## 開發慣例

### 後端代碼組織
- **工具函數**：放在 `app/tools/` 目錄下（如 `greeter.py`, `params_getter.py`）
- **資料模型**：Pydantic 模型放在 `app/models/models.py` 中
- **API 路由**：定義在 `app/main.py` 中

### 環境設定
- 機密與環境變數放在 `.env` 文件中（已被 git 忽略）
- 同步更新 `.env.example` 以文檔化所需的環境變數
- **必需環境變數**：
  - `CWA_API_KEY`：中央氣象局 API 金鑰（用於天氣功能）

### 前端開發
- 所有後端 API 呼叫統一經過 `src/api/client.ts`
- React 組件放在 `src/components/` 目錄（待建立）

### API 版本管理
- 破壞性 API 變更時使用版本前綴（`/api/v2` 等）
- 確保向後相容性或清晰的遷移路徑

## 環境變數配置

在 `backend/.env` 文件中設定以下變數：

```bash
# 中央氣象局 API（天氣功能）
CWA_API_KEY=your_cwa_api_key_here

# FastAPI 設定
DEBUG=false
```

參考 `backend/.env.example` 了解所有可用選項。

## 故障排除

### 1. 後端無法啟動
```bash
# 確保已安裝依賴
cd backend
pip install -r requirements.txt

# 檢查環境變數
cat .env
```

### 2. Docker Compose 構建失敗
```bash
# 清除快取並重新構建
docker-compose down -v
docker-compose up --build
```

### 3. 前端無法連接後端
- 確保後端在 http://localhost:8000 運行
- 檢查 `frontend/vite.config.ts` 中的代理設定

## 貢獻指南

1. 建立新分支：`git checkout -b feature/your-feature`
2. 提交變更：`git commit -m "簡要說明"`
3. 推送到遠端：`git push origin feature/your-feature`
4. 建立 Pull Request

## 許可證

MIT License
