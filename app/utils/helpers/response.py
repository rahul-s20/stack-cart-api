def response(data=None, message: str = '', status: bool = True, code: int = 200) -> dict:
    return {
        "status": status,
        "data": data,
        "code": code,
        "message": message,
    }


def error_response(error, code: int = 500, message: str = '', status: bool = False) -> dict:
    return {
        "status": status,
        "error": error,
        "code": code,
        "message": message
    }