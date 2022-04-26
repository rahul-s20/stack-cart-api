from fastapi import APIRouter
from . import *
from fastapi.encoders import jsonable_encoder

router = APIRouter()
role_obj = Roles()
merchant_obj = Merchants()


@router.post(ADD_ROLES)
async def add_roles(data: RolesSchema):
    res = await role_obj.add_update_role(role_data=jsonable_encoder(data))
    return res


@router.get(GET_ROLES)
async def get_all_roles():
    res = await role_obj.get_all_roles()
    return res


@router.post(CREATE_MERCHANT)
async def create_merchant(m_data: MerchantSchema):
    res = await merchant_obj.create_new_marchant(m_data=jsonable_encoder(m_data))
    return res


@router.put(UPDATE_MERCHANT)
async def update_merchant(_id, m_data: MerchantSchema):
    res = await merchant_obj.update_merchant(_id=_id, m_data=jsonable_encoder(m_data))
    return res


@router.put(DELETE_MERCHANT)
async def delete_merchant(_id):
    res = await merchant_obj.delete_merchant(_id=_id)
    return res
