from app.managers.merchants_data_manager import MerchantDM
from fastapi.responses import JSONResponse
from app.utils.helpers.response import response, error_response
from fastapi.encoders import jsonable_encoder


class Merchants:
    def __init__(self):
        self.__mdm = MerchantDM()

    async def fetch_all_merchants(self) -> JSONResponse:
        try:
            res = await self.__mdm.fetch_all_merchants()
            return JSONResponse(content=jsonable_encoder(response(data=res, message="All available merchants")))
        except Exception as er:
            return JSONResponse(content=jsonable_encoder(error_response(error=f"{er}", message="Something went "
                                                                                               "wrong")))

    def fetch_one_merchant(self):
        pass

    async def update_merchant(self, _id: str, m_data: dict) -> JSONResponse:
        try:
            res = await self.__mdm.update_merchant(_id=_id, m_data=m_data)
            if res is not None:
                return JSONResponse(content=jsonable_encoder(response(data=res, message="updated successfully")))
            else:
                return JSONResponse(content=jsonable_encoder(response(data=res, message="Merchant doesn't exists")))
        except Exception as er:
            return JSONResponse(content=jsonable_encoder(error_response(error=f"{er}", message="Something went "
                                                                                               "wrong")))

    async def delete_merchant(self, _id: str) -> JSONResponse:
        try:
            res = await self.__mdm.delete_one(_id=_id)
            if res is not None:
                return JSONResponse(
                    content=jsonable_encoder(response(data=res, message="Merchant deleted successfully")))
            elif res is None:
                return JSONResponse(
                    content=jsonable_encoder(response(data=res, message="It's not active, please create a Merchant")))
        except Exception as er:
            return JSONResponse(content=jsonable_encoder(error_response(error=f"{er}", message="Something went "
                                                                                               "wrong")))

    def update_merchant_status(self):
        pass

    async def create_new_marchant(self, m_data: dict) -> JSONResponse:
        try:
            res = await self.__mdm.add_merchant(m_data=m_data)
            return JSONResponse(content=jsonable_encoder(response(data=res, message="Merchant added successfully")))
        except Exception as er:
            return JSONResponse(content=jsonable_encoder(error_response(error=f"{er}", message="Something went "
                                                                                               "wrong")))
