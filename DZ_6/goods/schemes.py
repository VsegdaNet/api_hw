from pydantic import BaseModel, Field
from decimal import Decimal
from typing import Optional

# Базовая модель для товара
class GoodsBase(BaseModel):
    name: str = Field(..., alias="name_goods")
    description: str
    price: Decimal

    class Config:
        allow_population_by_field_name = True

# Модель для создания товара
class GoodsCreate(GoodsBase):
    pass

# Модель для обновления товара
class GoodsUpdate(GoodsBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None

# Модель для чтения товара из базы данных
class GoodsInDBBase(GoodsBase):
    id: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

# Модель для чтения товара
class Goods(GoodsInDBBase):
    pass