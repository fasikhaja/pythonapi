import datetime
from typing import Optional
from pydantic import BaseModel


class CPICVINs(BaseModel):

    cpic_id: int
    date_of_theft: Optional[datetime.date]
    recovered_date: Optional[str]
    theft_status_i_d: Optional[int]
    # expiry_date: Optional[datetime.date]
    # vehicle_type_i_d: Optional[int]
    # license_plate: Optional[str]
    # license_plate_province_i_d: Optional[int]
    # license_year: Optional[str]
    # v_i_n: Optional[str]
    # vehicle_model_year: Optional[str]
    # vehicle_make: Optional[str]
    # vehicle_model: Optional[str]
    # vehicle_color_exterior_i_d: Optional[int]
    # vehicle_color_interior_i_d: Optional[int]
    # vehicle_style: Optional[str]
    # i_b_c_vehicle_class: Optional[str]
    # i_b_c_vehicle_make: Optional[str]
    # i_b_c_vehicle_model: Optional[str]
    # i_b_c_vehicle_manufacturer: Optional[str]
    # v_i_n_validation_flag: Optional[str]
    # o_r_i_i_d: Optional[int]
    # created_on: datetime2 = sysdatetime()
    # created_by: str = original_login()
    # modified_on: datetime2 = sysdatetime()
    # modified_by: str = original_login()
