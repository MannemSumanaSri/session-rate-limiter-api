# app.py

from fastapi import FastAPI, HTTPException
from token_manager import TokenManager
from rate_limiter import RateLimiter

app = FastAPI()
token_manager = TokenManager()
rate_limiter = RateLimiter(max_requests=5, time_window_seconds=60)

@app.get("/")
def read_root():
    return {"message": "Session Token API with Rate Limiting"}

@app.post("/login")
def login():
    token = token_manager.generate_token(expiry_seconds=600)  # 10 minutes expiry
    return {"token": token, "expires_in_seconds": 600}

@app.get("/validate")
def validate(token: str):
    if not token_manager.validate_token(token):
        raise HTTPException(status_code=401, detail="Invalid or expired token.")
    return {"message": "Token is valid!"}

@app.get("/request_resource")
def request_resource(token: str):
    if not token_manager.validate_token(token):
        raise HTTPException(status_code=401, detail="Invalid or expired token.")

    if not rate_limiter.is_allowed(token):
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Try later.")

    return {"message": "Access granted to protected resource."}

@app.post("/logout")
def logout(token: str):
    token_manager.invalidate_token(token)
    return {"message": "Token invalidated successfully."}
