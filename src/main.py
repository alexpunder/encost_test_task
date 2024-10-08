from fastapi import FastAPI
from tortoise import Tortoise

from src.api import app as main_router
from src.config import settings


async def lifespan(app: FastAPI):
    await Tortoise.init(
        db_url=settings.database_url,
        modules={'models': ['src.models']}
    )
    await Tortoise.generate_schemas(safe=True)

    yield

    await Tortoise.close_connections()


app = FastAPI(
    title=settings.app_title,
    description=settings.description,
    lifespan=lifespan,
)

app.include_router(main_router)
