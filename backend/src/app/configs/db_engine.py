import os
from sqlalchemy import create_engine

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

db_dir = os.path.join(BASE_DIR, "database")
db_path = os.path.join(db_dir, "database.db")
os.makedirs(db_dir, exist_ok=True)
db_url = f"sqlite:///{db_path}"

engine = create_engine(db_url, echo=False)

