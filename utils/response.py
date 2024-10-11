from fastapi.responses import JSONResponse
from pydantic import BaseModel
from http import HTTPStatus


def success_response(message=None, data=None):
    if data and data != False:
        return JSONResponse(
            {'status_code': HTTPStatus.OK, 'detail': message, 'data': data},
            status_code=HTTPStatus.OK
        )
    return JSONResponse({'status_code': HTTPStatus.OK, 'detail': message}, status_code=HTTPStatus.OK)

def success_data_response(message=None, data=None):
    if data and data != False:
        return JSONResponse(
            {'status_code': HTTPStatus.OK, 'detail': message, 'data': data},
            status_code=HTTPStatus.OK
        )
    return JSONResponse(
            {'status_code': HTTPStatus.OK, 'detail': message, 'data': data},
            status_code=HTTPStatus.OK
        )
def bad_response(message=None):
    if message:
        return JSONResponse({'status_code':HTTPStatus.BAD_REQUEST,'detail': message}, status_code=HTTPStatus.BAD_REQUEST)
    return JSONResponse({'status_code':HTTPStatus.BAD_REQUEST,}, status_code=HTTPStatus.BAD_REQUEST)



def created_response(message, data=None):
    if data:
        return JSONResponse({'status_code':HTTPStatus.CREATED,'detail': message, 'data': data}, status_code=HTTPStatus.CREATED)
    return JSONResponse({'status_code':HTTPStatus.CREATED,'detail': message}, status_code=HTTPStatus.CREATED)
