from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from core.config import settings

class DbHelper:
    def __init__(self, url: str,
                 max_overflow: int = 10,
                 pool_size: int = 5,
                 echo: bool = True
                 ):
        self.engine = create_async_engine(
            url=url,
            max_overflow=max_overflow,
            pool_size=pool_size,
            echo=echo
        )

        self.session_factorio = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
         )

    async def dispose(self):
        await self.engine.dispose()

    async def session_getter(self):
        async with self.session_factorio() as session:
            yield session

db_helper = DbHelper(
    url=str(settings.db.url),
    max_overflow=settings.db.max_overflow[0],
    pool_size=settings.db.pool_size,
    echo=settings.db.echo
                 )