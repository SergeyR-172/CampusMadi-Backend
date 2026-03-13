import asyncio

from sqlalchemy import select

from core.database import database
from core.models.user import User
from api.jwt_auth.utils import hash_password

TEST_USERS = [
    {
        "username": "test_admin",
        "password": "admin123",
        "name": "Test Admin",
        "role": "admin",
    },
    {
        "username": "test_teacher",
        "password": "teacher123",
        "name": "Test teacher",
        "role": "teacher",
    },
    {
        "username": "test_user_1",
        "password": "user123",
        "name": "Test User 1",
        "role": "default",
    },
    {
        "username": "test_user_2",
        "password": "user123",
        "name": "Test User 2",
        "role": "default",
    },
]


async def create_test_users() -> None:
    async with database.session_fabric() as session:
        for user_data in TEST_USERS:
            stmt = select(User).where(User.username == user_data["username"])
            result = await session.execute(stmt)
            existing_user = result.scalars().first()

            if existing_user:
                print(f"[SKIP] User '{user_data['username']}' already exists")
                continue

            user = User(
                username=user_data["username"],
                hashed_password=hash_password(user_data["password"]),
                name=user_data["name"],
                role=user_data["role"],
            )
            session.add(user)
            print(
                f"[CREATE] username='{user_data['username']}', password='{user_data['password']}', role='{user_data['role']}'"
            )

        await session.commit()


if __name__ == "__main__":
    asyncio.run(create_test_users())
