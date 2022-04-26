from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class MerchantSchema(BaseModel):
    _id: Optional[str]
    name: str
    email: EmailStr
    phone_number: str
    brands: list
    business: str
    is_active: Optional[bool] = True
    status: Optional[str] = 'Waiting Approval'  # 'Waiting Approval', 'Rejected', 'Approved'
    created_at: Optional[datetime] = datetime.now()
    updated_on: Optional[datetime] = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "name": 'xyzw',
                "email": 'xyz@email.com',
                "phone_number": "9165327456",
                "brands": ["abc", "def"],
                "business": 'abc co',
            }
        }
