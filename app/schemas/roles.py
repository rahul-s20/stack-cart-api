from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class RolesSchema(BaseModel):
    _id: Optional[str]
    name: str
    is_active: Optional[bool] = True
    timestamp: Optional[datetime] = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "name": "member"
            }
        }
