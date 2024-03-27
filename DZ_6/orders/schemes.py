from pydantic import BaseModel
from datetime import date
from typing import Optional

class OrderBase(BaseModel):
    user_id: int
    product_id: int
    order_date: date
    status: str


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    user_id: Optional[int] = None
    product_id: Optional[int] = None
    order_date: Optional[date] = None
    status: Optional[str] = None


class OrderInDBBase(OrderBase):
    id: int

    class Config:
        orm_mode = True


class Order(OrderInDBBase):
    pass