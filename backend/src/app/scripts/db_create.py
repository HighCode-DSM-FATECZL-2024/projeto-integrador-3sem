import sys
import os

"""
  It will initialize the database, with the tables  
"""
try:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
    """ Essential to create the database (ENGINE and BASE for Tables) """
    from app.configs.database import engine
    from app.configs.database.base import Base

    # Table 'Users'
    from app.modules.auth.models import Users

    Base.metadata.create_all(bind=engine)
    print("Database created successfully.")
except Exception as err:
    print(f"Error occurred while creating the database: {err}")

