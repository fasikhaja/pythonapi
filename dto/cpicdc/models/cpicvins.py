from sqlalchemy import Column, Integer, String, Date, DateTime
import sqlalchemy as sa  # Importing sqlalchemy with alias

from database import Base

# class CPICVINs(Base):
#     __tablename__ = 'CPICVINs'

#     cpic_id = sa.Column("CPICID", sa.BigInteger(), primary_key=True)
#     date_of_theft = sa.Column("DateOfTheft", sa.Date())
#     recovered_date = sa.Column("RecoveredDate", sa.String(10))
#     theft_status_id = sa.Column("TheftStatusID", sa.Integer())


class CreateCPICVINs(Base):
    __tablename__ = "CPICVINs"
    
    CPICID = Column(Integer, primary_key=True, index=True)  
    DateOfTheft =Column(String(255), nullable=True)  
    RecoveredDate = Column(String(255), nullable=True)  
    TheftStatusID = Column(Integer, nullable=False)  
    ExpiryDate = Column(DateTime, nullable=True)  
    VehicleTypeID = Column(Integer, nullable=False)  
    LicensePlate = Column(String(255), nullable=False)  
    LicensePlateProvinceID = Column(Integer, nullable=True)  
    LicenseYear = Column(String(255), nullable=True)  
    VIN = Column(String(255), nullable=False)  
    VehicleModelYear = Column(String(255), nullable=True)  
    VehicleMake = Column(String(255), nullable=True)  
    VehicleModel = Column(String(255), nullable=True)  
    VehicleColorExteriorID = Column(Integer, nullable=True)  
    VehicleColorInteriorID = Column(Integer, nullable=True)  
    VehicleStyle = Column(String(255), nullable=True)  
    IBCVehicleClass = Column(String(255), nullable=True)  
    IBCVehicleMake = Column(String(255), nullable=True)  
    IBCVehicleModel = Column(String(255), nullable=True)  
    IBCVehicleManufacturer = Column(String(255), nullable=True)  
    VINValidationFlag = Column(String(255), nullable=True)  
    ORIID = Column(Integer, nullable=True)  
    CreatedOn = Column(DateTime, nullable=False)  
    CreatedBy = Column(String(255), nullable=False)  
    ModifiedOn = Column(DateTime, nullable=False)  
    ModifiedBy = Column(String(255), nullable=False)  