import os.path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

file_path = "database/reservationdb.db"


def check_if_database_exists():
    return os.path.exists(file_path)


def create_database():
    Base.metadata.create_all(engine)


engine = create_engine("sqlite:///" + file_path, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
