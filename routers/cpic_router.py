from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from database import get_db
from dto.cpicdc.schemas import cpicvins_schm
from dto.cpicdc.schemas.cpicvins_schm import CreateCPICVINRequest
from dto.cpicdc.models import cpicvins
from logger import logger
from utils.pagination import PagedResponseSchema, PageParams, paginate
from utils.response import created_response, bad_response, success_response, success_data_response
from crud.cpicvins import insert_cpicvin, get_cpicvins, delete_cpicvin_obj


router = APIRouter(prefix="/cpic", tags=["cpic"], )


@router.get("/cpicvins/", response_model=PagedResponseSchema[cpicvins_schm.CpicVinSchema])
def read_cpicvins(request: Request, page_params: PageParams = Depends(), db: Session = Depends(get_db)):
    logger.info("Fetch cpic vins")
    query = db.query(cpicvins.CPICVINs).order_by(cpicvins.CPICVINs.cpic_id)
    logger.debug("Created query")
    return paginate(page_params, query, cpicvins_schm.CpicVinSchema)

@router.post('/create')
def create_cpicvins(payload: CreateCPICVINRequest,  db: Session = Depends(get_db)):
    if not isinstance(payload, CreateCPICVINRequest):
        return bad_response("Invalid request data format")
    for field_name, field_value in payload.dict().items():
        if field_value and str(field_value).strip() == '':
            return bad_response(f"Please enter {field_name}")
    data = insert_cpicvin(db, payload)
    return created_response("Cpicvins added successfully!", data)

@router.get('/list')
def get_cpicvins_list(db: Session = Depends(get_db)):
    data = get_cpicvins(db)
    return success_data_response("success", data)

@router.delete('/delete/{id}')
async def delete_company(id:int, db: Session = Depends(get_db)):
    data = delete_cpicvin_obj(db, id)
    return success_response("Cpicvins deleted successfully!", 'data')