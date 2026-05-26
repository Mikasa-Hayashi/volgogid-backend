from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

DATABASE_URL = ""  # TODO: move to .env

engine = create_async_engine(DATABASE_URL, echo=False)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)
