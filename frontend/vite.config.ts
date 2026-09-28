import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// 開發時將 /api 代理到 FastAPI，避免 CORS 問題
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/api": "http://localhost:8000",
    },
  },
});
