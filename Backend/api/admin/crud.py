from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.user import User


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result = await session.execute(stmt)
    return list(result.scalars().all())


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    stmt = select(User).where(User.id == user_id)
    result = await session.execute(stmt)
    return result.scalars().first()


async def create_user(
    session: AsyncSession,
    username: str,
    hashed_password: str,
    name: str,
    role: str = "default",
) -> User:
    user = User(
        username=username,
        hashed_password=hashed_password,
        name=name,
        role=role,
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def update_user(
    session: AsyncSession,
    user_id: int,
    values: dict,
) -> User | None:
    if not values:
        return await get_user_by_id(session, user_id)

    stmt = update(User).where(User.id == user_id).values(**values)
    await session.execute(stmt)
    await session.commit()
    return await get_user_by_id(session, user_id)


async def delete_user(session: AsyncSession, user_id: int) -> bool:
    user = await get_user_by_id(session, user_id)
    if user is None:
        return False

    stmt = delete(User).where(User.id == user_id)
    await session.execute(stmt)
    await session.commit()
    return True
