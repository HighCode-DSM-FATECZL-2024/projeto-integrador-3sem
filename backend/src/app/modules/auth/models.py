from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm.exc import DetachedInstanceError

from app.configs.database.base import Base

class Users(Base):
    __tablename__ = "Users"

    id = Column(String, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    telephone = Column(Integer, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    def to_dict(self):
        try:
            return {
                'id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'telephone': self.telephone,
                'password': self.password,
                'created_at': self.created_at
            }
        except DetachedInstanceError:
            return {
                "error": "The database session has been closed."
            }
