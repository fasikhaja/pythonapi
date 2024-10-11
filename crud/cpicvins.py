from sqlalchemy.orm import Session
from dto.cpicdc.models import cpicvins as cpicvins_models
from crud.exceptions import ObjectDoesNotExistsException
from dto.cpicdc.models.cpicvins import CreateCPICVINs

def cpicvin_dict(obj):
    data = {
        "CPICID": str(obj.CPICID),
        "DateOfTheft": str(obj.DateOfTheft),
        "RecoveredDate": str(obj.RecoveredDate),
        "TheftStatusID": str(obj.TheftStatusID),
        "ExpiryDate": str(obj.ExpiryDate),
        "VehicleTypeID": str(obj.VehicleTypeID),
        "LicensePlate": str(obj.LicensePlate),
        "LicensePlateProvinceID": str(obj.LicensePlateProvinceID),
        "LicenseYear": str(obj.LicenseYear),
        "VIN": str(obj.VIN),
        "VehicleModelYear": str(obj.VehicleModelYear),
        "VehicleMake": str(obj.VehicleMake),
        "VehicleModel": str(obj.VehicleModel),
        "VehicleColorExteriorID": str(obj.VehicleColorExteriorID),
        "VehicleColorInteriorID": str(obj.VehicleColorInteriorID),
        "VehicleStyle": str(obj.VehicleStyle),
        "IBCVehicleClass": str(obj.IBCVehicleClass),
        "IBCVehicleMake": str(obj.IBCVehicleMake),
        "IBCVehicleModel": str(obj.IBCVehicleModel),
        "IBCVehicleManufacturer": str(obj.IBCVehicleManufacturer),
        "VINValidationFlag": str(obj.VINValidationFlag),
        "ORIID": str(obj.ORIID),
        "CreatedOn": str(obj.CreatedOn),
        "CreatedBy": str(obj.CreatedBy),
        "ModifiedOn": str(obj.ModifiedOn),
        "ModifiedBy": str(obj.ModifiedBy)
    }
    return data

def get_db_cpicvins(db: Session, skip:int=0, limit:int=100):
    return db.query(cpicvins_models.CPICVINs).all()

from datetime import datetime

def insert_cpicvin(db, data):
    data_dict = data.dict()
    data_dict['CreatedOn'] = datetime.now()
    data_dict['ModifiedOn'] = datetime.now()
    obj = CreateCPICVINs(**data_dict)
    db.add(obj)
    db.flush() 
    db.commit()
    data = cpicvin_dict(obj)
    return data

def get_cpicvins(db):
    array = []
    data = db.query(CreateCPICVINs).all()
    for i in data:
        array.append(cpicvin_dict(i))
    return array



def delete_cpicvin_obj(db, id):
    obj = db.query(CreateCPICVINs).filter(CreateCPICVINs.CPICID == id).first()
    if not obj:  
        raise ObjectDoesNotExistsException()
    db.delete(obj)
    db.commit()    
    return obj
