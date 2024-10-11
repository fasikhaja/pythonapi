import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class CPICVINs(Base):

    __tablename__ = 'CPICVINs'

    cpic_id = sa.Column(" ", sa.BigInteger(), primary_key=True)
    date_of_theft = sa.Column("DateOfTheft", sa.Date())
    recovered_date = sa.Column(sa.String(10))
    theft_status_i_d = sa.Column("TheftStatusID", sa.Integer())
    # expiry_date = sa.Column(sa.Date())
    # vehicle_type_i_d = sa.Column(sa.Integer())
    # license_plate = sa.Column(sa.String(100))
    # license_plate_province_i_d = sa.Column(sa.Integer())
    # license_year = sa.Column(sa.String(10))
    # v_i_n = sa.Column(sa.String(20))
    # vehicle_model_year = sa.Column(sa.String(10))
    # vehicle_make = sa.Column(sa.String(100))
    # vehicle_model = sa.Column(sa.String(100))
    # vehicle_color_exterior_i_d = sa.Column(sa.Integer())
    # vehicle_color_interior_i_d = sa.Column(sa.Integer())
    # vehicle_style = sa.Column(sa.String(100))
    # i_b_c_vehicle_class = sa.Column(sa.String(50))
    # i_b_c_vehicle_make = sa.Column(sa.String(50))
    # i_b_c_vehicle_model = sa.Column(sa.String(50))
    # i_b_c_vehicle_manufacturer = sa.Column(sa.String(50))
    # v_i_n_validation_flag = sa.Column(sa.String(1))
    # o_r_i_i_d = sa.Column(sa.Integer())
    # created_on = sa.Column(datetime2(3), nullable=False, server_default='sysdatetime()')
    # created_by = sa.Column(sa.String(50), nullable=False, server_default='original_login()')
    # modified_on = sa.Column(datetime2(3), nullable=False, server_default='sysdatetime()')
    # modified_by = sa.Column(sa.String(50), nullable=False, server_default='original_login()')
