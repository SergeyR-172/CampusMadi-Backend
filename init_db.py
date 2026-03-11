import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from core.settings import settings
from core.models import Base

async def create_tables():
    engine = create_async_engine(settings.db_url)
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def main():
    retries = 5
    while retries > 0:
        try:
            await create_tables()
            break
        except Exception as e:
            retries -= 1
            print(f"Database connection failed, retrying... ({retries} attempts left): {e}")
            await asyncio.sleep(2)
    else:
        print("Failed to connect to database after multiple attempts")
        raise Exception("Could not initialize database")

if __name__ == "__main__":
    asyncio.run(main())