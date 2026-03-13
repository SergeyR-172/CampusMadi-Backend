from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from .schemas import *

from core.database import database
from core.models.user import User
from api.jwt_auth import dependencies as auth_dp
from api.jwt_auth.utils import hash_password
from api.jwt_auth.crud import get_user_by_username
from . import crud


router = APIRouter(prefix="/api/admin", tags=["Admin"])


isAdmin = Annotated[User, Depends(auth_dp.is_admin)]

@router.get(
    "/users",
    response_model=list[UserOut],
    summary="Получить список пользователей",
    description="Возвращает список всех пользователей. Доступно только администратору.",
)
async def list_users(
    _: isAdmin,
    session: AsyncSession = Depends(database.get_session),
):
    return await crud.get_users(session)


@router.get(
    "/users/{user_id}",
    response_model=UserOut,
    summary="Получить пользователя по ID",
    description="Возвращает пользователя по идентификатору. Доступно только администратору.",
)
async def get_user(
    user_id: int,
    _: isAdmin,
    session: AsyncSession = Depends(database.get_session),
):
    user = await crud.get_user_by_id(session, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.post(
    "/users",
    response_model=UserOut,
    summary="Создать пользователя",
    description="Создает нового пользователя с указанной ролью. Доступно только администратору.",
)
async def create_user(
    user_data: UserCreate,
    _: isAdmin,
    session: AsyncSession = Depends(database.get_session),
):
    from api.jwt_auth.crud import get_user_by_username

    if await get_user_by_username(session, user_data.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )

    return await crud.create_user(
        session=session,
        username=user_data.username,
        hashed_password=hash_password(user_data.password),
        name=user_data.name,
        role=user_data.role,
    )


@router.patch(
    "/users/{user_id}",
    response_model=UserOut,
    summary="Обновить пользователя",
    description="Частично обновляет данные пользователя (username, password, name, role). Доступно только администратору.",
)
async def update_user(
    user_id: int,
    user_data: UserUpdate,
    _: isAdmin,
    session: AsyncSession = Depends(database.get_session),
):
    current_user = await crud.get_user_by_id(session, user_id)
    if current_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    values = user_data.model_dump(exclude_unset=True)
    if "password" in values:
        values["hashed_password"] = hash_password(values.pop("password"))

    if "username" in values and values["username"] != current_user.username:
        if await get_user_by_username(session, values["username"]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists",
            )

    updated = await crud.update_user(session, user_id, values)
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return updated


@router.delete(
    "/users/{user_id}",
    summary="Удалить пользователя",
    description="Удаляет пользователя по идентификатору. Доступно только администратору.",
)
async def delete_user(
    user_id: int,
    _: isAdmin,
    session: AsyncSession = Depends(database.get_session),
):
    deleted = await crud.delete_user(session, user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
