import asyncio
from tortoise import Tortoise


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'db': ['db']}
    )
    await Tortoise.generate_schemas()


async def main():
    await init()


if __name__ == "__main__":
    asyncio.run(main())
