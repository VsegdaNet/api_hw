# crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from orders import models
from orders import schemes

# CRUD для таблицы Orders


async def get_order(db: AsyncSession, order_id: int):
    query = select(models.Order).where(models.Order.id == order_id)
    result = await db.execute(query)
    return result.scalars().first()


async def create_order(db: AsyncSession, order: schemes.OrderCreate):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)
    return db_order


async def update_order(db: AsyncSession, db_order: models.Order, order: schemes.OrderUpdate):
    update_data = order.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_order, key, value)
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)
    return db_order


async def delete_order(db: AsyncSession, order_id: int):
    query = select(models.Order).where(models.Order.id == order_id)
    result = await db.execute(query)
    order = result.scalars().first()
    if order:
        await db.delete(order)
        await db.commit()
    return order

