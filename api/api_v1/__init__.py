from fastapi import APIRouter
from core.config import settings

from .users import router as user_router

router =  APIRouter(
     prefix=settings.prefix.api_v1.version
)

router.include_router(user_router, prefix=settings.prefix.api_v1.users)