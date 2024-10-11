
# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker

# SQLALCHEMY_DATABASE_URL = (
#     "mssql+pyodbc://admin:Welcome1!@15.223.70.0/CPICDB"
#     "?driver=ODBC+Driver+17+for+SQL+Server"
# )

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     connect_args={"check_same_thread": False},  # only needed for SQLite
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# # Database setup
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# MySQL database connection URL using PyMySQL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/test"

# Create an engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
