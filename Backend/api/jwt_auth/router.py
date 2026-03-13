from fastapi import APIRouter, Depends, Response, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone, timedelta

from core.database import database

from .schemas import UserSchema, TokenInfo, UserLogin
from .utils import validate_password, create_access_token, create_refresh_token
from . import crud
from . import dependencies as dp

router = APIRouter(tags=["JWT_Auth"], prefix="/api/jwt")

@router.get("/me", response_model=UserSchema)
async def get_me(user = Depends(dp.get_current_user)):
    return user

@router.post("/login", response_model=TokenInfo)
async def auth_user_jwt(
    response: Response,
    user_data: UserLogin,
    session: AsyncSession = Depends(database.get_session)
):
    user = await crud.get_user_by_username(session, user_data.username)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
        )
    
    if not validate_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
        )
    
    jwt_payload = {
        "sub": str(user.id),
        "username": user.username,
        "role": user.role
    }
    access_token = create_access_token(payload=jwt_payload)
    refresh_token, refresh_token_hash = create_refresh_token()
    

    expires_at = datetime.now(timezone.utc) + timedelta(days=30)
    await crud.create_refresh_token(session, user.id, refresh_token_hash, expires_at)
    

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=2592000  # 30 дней в секундах
    )
    
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="lax",
    )
    
    return TokenInfo(
        access_token=access_token,
        token_type="Bearer",
    )