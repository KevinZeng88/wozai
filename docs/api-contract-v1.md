# API Contract V1 (Draft)

## GET /health
Response:
```json
{ "status": "ok" }
```

## POST /api/auth/send-code
Request:
```json
{ "email": "user@example.com" }
```
Response:
```json
{ "request_id": "string", "cooldown_seconds": 60 }
```

## POST /api/auth/verify-code
Request:
```json
{ "email": "user@example.com", "code": "123456" }
```
Success response:
```json
{ "access_token": "string", "refresh_token": "string", "user_id": "string" }
```
Error response:
```json
{ "error": "code_not_found|code_expired|code_invalid" }
```
