# 我在 (wozai.org)

“我在”是一个记录人生与数字纪念的原型项目。V1 目标是提供可运行的前后端骨架与核心产品方案文档，后续逐步实现端到端加密、身后触发流程和清明线上悼念活动。

## Repository Structure

- `frontend/`: Vite + Vue 3 + TypeScript
- `backend/`: FastAPI + Python
- `docs/`: 产品、安全、API、路线图文档

## Quick Start

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn app.main:app --reload
```

Backend health check:

```bash
curl http://127.0.0.1:8000/health
```

## Core Principles

- 用户拥有数据主权
- 默认零知识存储（服务端只存密文）
- 未经用户授权，管理员不可读取私密内容
- 面向中文文化语境，支持清明节线上悼念
