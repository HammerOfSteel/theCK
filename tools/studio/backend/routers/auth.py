"""Authentication API routes — login, logout, register, user management."""

from fastapi import APIRouter, Request, Response
from pydantic import BaseModel

from backend import database as db

router = APIRouter(prefix="/api/auth", tags=["auth"])


class LoginRequest(BaseModel):
    username: str
    password: str


class RegisterRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(req: LoginRequest, response: Response):
    """Authenticate user and set session cookie."""
    user = db.verify_user(req.username, req.password)
    if not user:
        return {"ok": False, "error": "Invalid username or password"}

    token = db.create_session(user["id"])
    response.set_cookie(
        key="session",
        value=token,
        httponly=True,
        samesite="lax",
        max_age=db.SESSION_TTL,
    )
    return {"ok": True, "user": {"username": user["username"], "role": user["role"]}}


@router.post("/logout")
def logout(request: Request, response: Response):
    """Clear session."""
    token = request.cookies.get("session")
    if token:
        db.delete_session(token)
    response.delete_cookie("session")
    return {"ok": True}


@router.post("/register")
def register(req: RegisterRequest):
    """Register a new admin user."""
    if len(req.username.strip()) < 2:
        return {"ok": False, "error": "Username must be at least 2 characters"}
    if len(req.password) < 4:
        return {"ok": False, "error": "Password must be at least 4 characters"}

    user = db.create_user(req.username, req.password, role="admin")
    if not user:
        return {"ok": False, "error": "Username already taken"}

    return {"ok": True, "user": {"username": user["username"], "role": user["role"]}}


@router.get("/me")
def current_user(request: Request):
    """Get current logged-in user from session cookie."""
    token = request.cookies.get("session")
    user = db.validate_session(token)
    if user:
        return {"authenticated": True, "user": {"username": user["username"], "role": user["role"]}}
    return {"authenticated": False}


@router.get("/users")
def list_users(request: Request):
    """List all users (admin only)."""
    token = request.cookies.get("session")
    user = db.validate_session(token)
    if not user:
        return {"ok": False, "error": "Not authenticated"}
    return {"ok": True, "users": db.list_users()}
