from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from goods import models
from goods import schemes

# CRUD для таблицы Goods


async def get_good(db: AsyncSession, good_id: int):
    query = select(models.Goods).where(models.Goods.id == good_id)
    result = await db.execute(query)
    return result.scalars().first()


async def create_good(db: AsyncSession, good: schemes.GoodsCreate):
    db_good = models.Goods(**good.dict())
    db.add(db_good)
    await db.commit()
    await db.refresh(db_good)
    return db_good


async def update_good(db: AsyncSession, db_good: models.Goods, good: schemes.GoodsUpdate):
    update_data = good.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_good, key, value)
    db.add(db_good)
    await db.commit()
    await db.refresh(db_good)
    return db_good


async def delete_good(db: AsyncSession, good_id: int):
    query = select(models.Goods).where(models.Goods.id == good_id)
    result = await db.execute(query)
    good = result.scalars().first()
    if good:
        await db.delete(good)
        await db.commit()
    return good