from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductSchema(BaseModel):
    _id: Optional[str]
    sku: str
    name: str
    slug: Optional[str]
    image_url: str
    description: str
    quantity: int
    price: str
    discount: str
    actual_price: str
    taxable: Optional[bool] = True
    is_active: Optional[bool] = True
    brand: str
    created_at: Optional[datetime] = datetime.now()
    updated_on: Optional[datetime] = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "sku": "123456",
                "name": 'xyz',
                "image_url": 'gdh.jpg',
                "description": 'abc',
                "quantity": 100,
                "price": "199.00",
                "discount": "50.00",
                "actual_price": "249.00",
                "brand": "123456",
            }
        }
