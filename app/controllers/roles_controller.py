from app.managers.roles_data_manager import RolesDM
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.utils.helpers.response import response, error_response


class Roles:
    def __init__(self):
        self.rdm = RolesDM()

    async def add_update_role(self, role_data: dict) -> JSONResponse:
        try:
            res = await self.rdm.add_role(roles_data=role_data)
            return JSONResponse(content=jsonable_encoder(response(data=res, message="Roles updated successfully")))
        except Exception as er:
            return JSONResponse(content=jsonable_encoder(error_response(error=f"{er}", message="Something went "
                                                                                               "wrong")))

    async def get_all_roles(self):
        try:
            res = await self.rdm.get_all_roles()
            return JSONResponse(content=jsonable_encoder(response(data=res, message="All roles")))
        except Exception as er:
            return JSONResponse(content=jsonable_encoder(error_response(error=f"{er}", message="Something went "
                                                                                               "wrong")))