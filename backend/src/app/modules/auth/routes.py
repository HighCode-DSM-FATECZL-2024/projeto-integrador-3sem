from fastapi import APIRouter
from .schemas import UserCreateValidator
from app.core.utils.passwords import Passwords
from app.core.utils.uuid_generator import UUIDGenerator
from .exceptions import *


auth = APIRouter(prefix="/auth", tags=["Authentication"])

@auth.post("/login")
async def login(): pass

@auth.post("/logout")
async def logout(): pass


@auth.post("/signup")
async def register(body_user: UserCreateValidator):
    """ Register Users """

    """ Verify Passwords Match """
    match_passwords = Passwords.verify_passwords_match(body_user.password, body_user.confirm_password)
    if not match_passwords:
        raise PasswordsDoNotMatchException()

    """ Generate a Unique Identifier """
    identifier = UUIDGenerator.generate_identifier()
    print(identifier)

    return {"message": body_user}
