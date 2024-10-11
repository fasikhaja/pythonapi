USE test;

CREATE TABLE IF NOT EXISTS ORI (
    ORIID INT PRIMARY KEY,
    SomeOtherColumn VARCHAR(255) 
);

CREATE TABLE IF NOT EXISTS CPICVINs (
    CPICID BIGINT AUTO_INCREMENT NOT NULL,
    DateOfTheft VARCHAR(255) NOT NULL,
    RecoveredDate VARCHAR(255) NULL, 
    TheftStatusID INT NOT NULL,
    ExpiryDate VARCHAR(255) NULL,
    VehicleTypeID INT NOT NULL,
    LicensePlate VARCHAR(255) NOT NULL, 
    LicensePlateProvinceID INT NULL,
    LicenseYear VARCHAR(255) NULL, 
    VIN VARCHAR(255) NOT NULL, 
    VehicleModelYear VARCHAR(255) NULL, 
    VehicleMake VARCHAR(255) NULL, 
    VehicleModel VARCHAR(255) NULL, 
    VehicleColorExteriorID INT NULL,
    VehicleColorInteriorID INT NULL,
    VehicleStyle VARCHAR(255) NULL, 
    IBCVehicleClass VARCHAR(255) NULL, 
    IBCVehicleMake VARCHAR(255) NULL, 
    IBCVehicleModel VARCHAR(255) NULL, 
    IBCVehicleManufacturer VARCHAR(255) NULL, 
    VINValidationFlag CHAR(255) NULL, 
    ORIID INT NULL,
    CreatedOn DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CreatedBy VARCHAR(255) NOT NULL, 
    ModifiedOn DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
    ModifiedBy VARCHAR(255) NOT NULL, 
    PRIMARY KEY (CPICID),
    FOREIGN KEY (ORIID) REFERENCES ORI(ORIID)
)