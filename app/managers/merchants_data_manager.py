from app.db_config.db import create_db
from app.configs.constants import MERCHANT_COLLECTION, MERCHANT_STATUS
from bson.objectid import ObjectId


def merchant_helper(obj) -> dict:
    return {
        "id": str(obj["_id"]),
        "name": obj["name"],
        "email": obj["email"],
        "phone_number": obj["phone_number"],
        "brands": obj["brands"],
        "business": obj["business"],
        "status": obj["status"]
    }


class MerchantDM:
    def __init__(self) -> None:
        self.__merchant_coll = create_db().get_collection(MERCHANT_COLLECTION)

    async def fetch_all_merchants(self):
        all_merchants = list()
        async for mer in self.__merchant_coll.find():
            all_merchants.append(merchant_helper(mer))
        return all_merchants

    async def fetch_one(self, _id: str):
        existing_merchant = await self.__merchant_coll.find_one({"_id": ObjectId(_id)})
        if existing_merchant:
            return merchant_helper(existing_merchant)
        else:
            return None

    async def delete_one(self, _id: str):
        existing_m = await self.__merchant_coll.find_one({"_id": ObjectId(_id)})
        if existing_m and existing_m["is_active"] is True:
            existing_m["is_active"] = False
            await self.__merchant_coll.update_one({"_id": ObjectId(existing_m["_id"])}, {"$set": existing_m})
            return "Merchant deleted successfully"
        else:
            return None

    async def update_merchant(self, _id: str, m_data: dict):
        existing_m = await self.__merchant_coll.find_one({"_id": ObjectId(_id)})
        if existing_m and existing_m["is_active"] is True and m_data["status"] == MERCHANT_STATUS["WA"]:
            await self.__merchant_coll.update_one({"_id": ObjectId(existing_m["_id"])}, {"$set": m_data})
            updated_merchant = await self.__merchant_coll.find_one({"_id": ObjectId(existing_m["_id"])})
            return merchant_helper(updated_merchant)
        elif existing_m and existing_m["is_active"] is True and m_data["status"] != MERCHANT_STATUS["WA"]:
            m_data["status"] = MERCHANT_STATUS["WA"]
            await self.__merchant_coll.update_one({"_id": ObjectId(existing_m["_id"])}, {"$set": m_data})
            updated_merchant = await self.__merchant_coll.find_one({"_id": ObjectId(existing_m["_id"])})
            return merchant_helper(updated_merchant)
        else:
            return None

    async def add_merchant(self, m_data: dict):
        existing_merchant = await self.__merchant_coll.find_one({'$or': [{"email": m_data["email"]},
                                                                         {"phone_number": m_data["phone_number"]}]})
        if existing_merchant is None and m_data["status"] == MERCHANT_STATUS["WA"]:
            res = await self.__merchant_coll.insert_one(m_data)
            new_merchant = await self.__merchant_coll.find_one({"_id": res.inserted_id})
            return merchant_helper(new_merchant)
        elif existing_merchant is None and m_data["status"] != MERCHANT_STATUS["WA"]:
            return "You are not allowed to change the status"
        elif existing_merchant:
            return "You already exists"



