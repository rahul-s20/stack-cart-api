import motor.motor_asyncio
from app.configs.settings import MONGODB_URI, DB_NAME


def create_db():
    try:
        client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
        db = client[DB_NAME]
        return db
    except Exception as er:
        raise er.__cause__
