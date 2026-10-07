from fastapi import FastAPI
import uvicorn

from api import router

from core.config import settings
from core.models import db_helper

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
     yield

     await db_helper.dispose()

app = FastAPI(lifespan=lifespan)
app.include_router(
    router,
    prefix=settings.prefix.api
   )

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.run.ip, port=settings.run.port, reload=True)