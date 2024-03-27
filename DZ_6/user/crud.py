# crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from user import models
from user import schemes

async def get_user_by_email(db: AsyncSession, email: str):
    query = select(models.User).where(models.User.email == email)
    result = await db.execute(query)
    return result.scalars().first()


async def get_user(db: AsyncSession, user_id: int):
    query = select(models.User).where(models.User.id == user_id)
    result = await db.execute(query)
    return result.scalars().first()


async def create_user(db: AsyncSession, user: schemes.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def update_user(db: AsyncSession, db_user: models.User, user: schemes.UserUpdate):
    update_data = user.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def delete_user(db: AsyncSession, user_id: int):
    query = select(models.User).where(models.User.id == user_id)
    result = await db.execute(query)
    user = result.scalars().first()
    if user:
        await db.delete(user)
        await db.commit()
    return user