import asyncpg

from booking.settings import get_settings

settings = get_settings()


class Db:
    async def make_engine():
        return await asyncpg.create_pool(dsn=settings.database_url, command_timeout=60)

    async def make_session_factory(engine):
        pass
