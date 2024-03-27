from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from user import crud
from goods import crud
from orders import crud
from user import schemes
from goods import schemes
from orders import schemes
from db import async_session_maker

app = FastAPI()



async def get_db():
    async with async_session_maker() as session:
        yield session

# Маршруты для таблицы Users
@app.post("/users/", response_model=schemes.User)
async def create_user(user: schemes.UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemes.User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=schemes.User)
async def update_user(user_id: int, user: schemes.UserUpdate, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud.update_user(db=db, db_user=db_user, user=user)

@app.delete("/users/{user_id}", response_model=schemes.User)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud.delete_user(db=db, user_id=user_id)


# Маршруты для таблицы Goods
@app.post("/goods/", response_model=schemes.Goods)
async def create_good(good: schemes.GoodsCreate, db: AsyncSession = Depends(get_db)):
    db_good = await crud.get_good_by_name(db, name=good.name)
    if db_good:
        raise HTTPException(status_code=400, detail="Good already exists")
    return await crud.create_good(db=db, good=good)

@app.get("/goods/{good_id}", response_model=schemes.Goods)
async def read_good(good_id: int, db: AsyncSession = Depends(get_db)):
    db_good = await crud.get_good(db, good_id=good_id)
    if db_good is None:
        raise HTTPException(status_code=404, detail="Good not found")
    return db_good

@app.put("/goods/{good_id}", response_model=schemes.Goods)
async def update_good(good_id: int, good: schemes.GoodsUpdate, db: AsyncSession = Depends(get_db)):
    db_good = await crud.get_good(db, good_id=good_id)
    if db_good is None:
        raise HTTPException(status_code=404, detail="Good not found")
    return await crud.update_good(db=db, db_good=db_good, good=good)

@app.delete("/goods/{good_id}", response_model=schemes.Goods)
async def delete_good(good_id: int, db: AsyncSession = Depends(get_db)):
    db_good = await crud.get_good(db, good_id=good_id)
    if db_good is None:
        raise HTTPException(status_code=404, detail="Good not found")
    return await crud.delete_good(db=db, good_id=good_id)

# Маршруты для таблицы Orders
@app.post("/orders/", response_model=schemes.Order)
async def create_order(order: schemes.OrderCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_order(db=db, order=order)

@app.get("/orders/{order_id}", response_model=schemes.Order)
async def read_order(order_id: int, db: AsyncSession = Depends(get_db)):
    db_order = await crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@app.put("/orders/{order_id}", response_model=schemes.Order)
async def update_order(order_id: int, order: schemes.OrderUpdate, db: AsyncSession = Depends(get_db)):
    db_order = await crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return await crud.update_order(db=db, db_order=db_order, order=order)

@app.delete("/orders/{order_id}", response_model=schemes.Order)
async def delete_order(order_id: int, db: AsyncSession = Depends(get_db)):
    db_order = await crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return await crud.delete_order(db=db, order_id=order_id)