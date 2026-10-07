from typing import Sequence, TYPE_CHECKING

if TYPE_CHECKING:
     from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select

from sqlalchemy.exc import IntegrityError

from core.models import User
from core.schemas import UserCreate, UserRead

from fastapi import HTTPException

async def create_users(
          session: AsyncSession,
          user_crete: UserCreate
                       ) -> User:
     try:
          user = User(username=user_crete.username, password=user_crete.password)
          session.add(user)
          await session.commit()
     except IntegrityError as ex:
         if ex.args[0] == '(sqlalchemy.dialects.postgresql.asyncpg.UniqueViolationError) повторяющееся значение ключа нарушает ограничение уникальности "users_username_key"':
             raise HTTPException(status_code=409, detail=f"The username {user_crete.username} already exist")

     # await session.refresh(user)
     return user

async def get_current_user(
        session: AsyncSession,
        cred: UserRead
) -> User:
     stmt = select(User.id, User.username).where(User.id == cred.id)
     user = await session.scalar(stmt)

     return user