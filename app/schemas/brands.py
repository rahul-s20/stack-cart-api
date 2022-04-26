from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BrandSchema(BaseModel):
    _id: Optional[str]
    name: str
    slug: Optional[str]
    image_url: str
    merchant: str
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = datetime.now()
    updated_on: Optional[datetime] = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "name": 'xyzw',
                "image_url": 'gdh.jpg',
                "merchant": "123456"
            }
        }
