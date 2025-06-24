from functools import wraps
from app.configs.db_session import session

"""
    This decorator is responsible for managing the database session, committing and closing.
"""
def session_management(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        db_session = session()
        try:
            result = func(db_session, *args, **kwargs)
            db_session.commit()
            return result
        except Exception:
            db_session.rollback()
            raise
        finally:
            db_session.close()
    return wrapper