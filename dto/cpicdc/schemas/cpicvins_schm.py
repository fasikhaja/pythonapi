from datetime import datetime  
from typing import Optional
from pydantic import BaseModel, ConfigDict

class CpicVinSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    cpic_id: int
    date_of_theft: Optional[datetime]  
    recovered_date: Optional[str]
    theft_status_id: Optional[int]

    class Config:
        orm_mode = True

class CreateCPICVINRequest(BaseModel):
    DateOfTheft: Optional[str]  
    RecoveredDate: Optional[str] 
    ExpiryDate: Optional[str] 
    TheftStatusID: int
    VehicleTypeID: int
    LicensePlate: str
    LicensePlateProvinceID: int
    LicenseYear: str
    VIN: str
    VehicleModelYear: str
    VehicleMake: str
    VehicleModel: str
    VehicleColorExteriorID: int
    VehicleColorInteriorID: int
    VehicleStyle: str
    IBCVehicleClass: str
    IBCVehicleMake: str
    IBCVehicleModel: str
    IBCVehicleManufacturer: str
    VINValidationFlag: str
    ORIID: int
    CreatedOn: Optional[datetime]
    CreatedBy: str
    ModifiedOn: Optional[datetime]
    ModifiedBy: str
