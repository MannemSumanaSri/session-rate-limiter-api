# Session-Based Token API with Rate Limiter (O(1) Backend Logic)

This project demonstrates:
- **O(1) session token management** using Python dictionaries.
- **O(1) rate limiting per token/user**.
- Backend API built using FastAPI.

---

## Features:
- Generate session token (`/login`)
- Validate session token (`/validate`)
- Access rate-limited endpoint (`/request_resource`)
- Invalidate token (`/logout`)

---

## Why O(1)?
- Token validation uses direct dictionary lookups.
- Rate limiter uses direct dictionary updates.
- Ensures constant-time operations for backend performance.

---

## How to Run:
```bash
pip install -r requirements.txt
uvicorn app:app --reload
