from app.db_config.db import create_db
from app.configs.constants import ROLES_COLLECTION
from bson.objectid import ObjectId


def role_helper(obj) -> dict:
    return {
        "id": str(obj["_id"]),
        "name": obj["name"],
        "is_active": obj["is_active"]
    }


class RolesDM:
    def __init__(self):
        self.__roles_coll = create_db().get_collection(ROLES_COLLECTION)

    async def __find_role_by_att__(self, key: str, value: str):
        return await self.__roles_coll.find_one({f"{key}": value})

    async def add_role(self, roles_data: dict):
        role = await self.__roles_coll.find_one({"name": roles_data["name"]})
        if role is None:
            res = await self.__roles_coll.insert_one(roles_data)
            new_role = await self.__roles_coll.find_one({"_id": res.inserted_id})
            return role_helper(new_role)
        else:
            await self.__roles_coll.update_one({"_id": ObjectId(role["_id"])}, {"$set": roles_data})
            updated_role = await self.__roles_coll.find_one({"_id": ObjectId(role["_id"])})
            return role_helper(updated_role)

    async def get_all_roles(self):
        all_roles = list()
        async for role in self.__roles_coll.find():
            all_roles.append(role_helper(role))
        return all_roles
