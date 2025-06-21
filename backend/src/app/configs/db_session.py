from sqlalchemy.orm import sessionmaker
from app.configs.db_engine import engine

session = sessionmaker(bind=engine)