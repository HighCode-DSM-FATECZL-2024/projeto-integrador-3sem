from typing import Optional, Tuple

from app.core.decorators.db_management import session_management
from .models import Users

class AuthService:
    @staticmethod
    @session_management
    def create_user(session, data) -> bool:
        """ Will register the user in the database. """
        if data:
            user = Users(**data)
            session.add(user)
            return True
        return False

    @staticmethod
    @session_management
    def search_email(session, email: str) -> Tuple[bool, Optional[Users]]:
        """Search for a user by email."""
        if not email:
            return False, None
        user = session.query(Users).filter(Users.email == email).first()
        if user:
            return True, user
        return False, None

    @staticmethod
    @session_management
    def search_telephone(session, telephone: int) -> Tuple[bool, Optional[Users]]:
        """Search for a user by telephone."""
        if not telephone:
            return False, None
        phone = session.query(Users).filter(Users.telephone == telephone).first()
        if phone:
            return True, phone
        return False, None