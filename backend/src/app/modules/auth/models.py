from sqlalchemy import Column, Integer, String

from app.configs.db_base import Base

class Users(Base):
    __tablename__ = "Users"

    id = Column(String, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    telephone = Column(Integer, nullable=False, unique=True)
    password = Column(String, nullable=False)