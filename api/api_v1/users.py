from fastapi import (
     APIRouter,
     Depends
)

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper

from core.schemas import UserCreate, UserRead
from crud.users import create_users, get_current_user

router = APIRouter(tags=["Users"])

@router.post("/create_user",)
async def create_user(
        user_create: UserCreate,
        session: AsyncSession = Depends(db_helper.session_getter)
                      ):
     user = await create_users(session=session, user_crete=user_create)
     return user
