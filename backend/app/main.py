from datetime import UTC, datetime, timedelta
from secrets import token_hex

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI(title="wozai-backend", version="0.1.0")


class SendCodeRequest(BaseModel):
    email: EmailStr


class VerifyCodeRequest(BaseModel):
    email: EmailStr
    code: str


# Prototype-only ephemeral storage.
codes: dict[str, dict[str, datetime | str]] = {}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/auth/send-code")
def send_code(payload: SendCodeRequest) -> dict[str, int | str]:
    code = token_hex(3)
    expires_at = datetime.now(UTC) + timedelta(minutes=10)
    codes[payload.email] = {"code": code, "expires_at": expires_at}
    return {"request_id": token_hex(8), "cooldown_seconds": 60}


@app.post("/api/auth/verify-code")
def verify_code(payload: VerifyCodeRequest) -> dict[str, str]:
    entry = codes.get(payload.email)
    if not entry:
        return {"error": "code_not_found"}

    if datetime.now(UTC) > entry["expires_at"]:
        return {"error": "code_expired"}

    if payload.code != entry["code"]:
        return {"error": "code_invalid"}

    return {
        "access_token": token_hex(24),
        "refresh_token": token_hex(24),
        "user_id": token_hex(8),
    }
