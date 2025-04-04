# import asyncio
# from sqlalchemy.ext.asyncio import create_async_engine
# from sqlalchemy import text


# async def test():
#     engine = create_async_engine(
#         "postgresql+asyncpg://postgres:goit@localhost:5432/contacts", echo=True
#     )
#     async with engine.connect() as conn:
#         result = await conn.execute(text("SELECT 1"))
#         print(result.scalar())


# asyncio.run(test())
