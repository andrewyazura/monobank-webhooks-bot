from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from .routes import monobank, telegram
from .telegram import telegram_api


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    await telegram_api.initialize()
    yield
    await telegram_api.shutdown()


def build_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    app.include_router(telegram.router)
    app.include_router(monobank.router)

    return app
