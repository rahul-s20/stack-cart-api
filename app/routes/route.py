from fastapi import APIRouter
from . import *
from fastapi.encoders import jsonable_encoder

router = APIRouter()
role_obj = Roles()


@router.post(ADD_ROLES)
async def add_roles(data: RolesSchema):
    res = await role_obj.add_update_role(role_data=jsonable_encoder(data))
    return res


@router.get(GET_ROLES)
async def get_all_roles():
    res = await role_obj.get_all_roles()
    return res
