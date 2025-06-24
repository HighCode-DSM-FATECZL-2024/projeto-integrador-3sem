from fastapi import APIRouter
from .schemas import *
from app.core.utils.passwords import Passwords
from app.core.utils.uuid_generator import UUIDGenerator
from .exceptions import *
from .services import *
from fastapi import status

auth = APIRouter(prefix="/auth", tags=["Authentication"])

@auth.post("/login")
async def login(body_user: UserLoginValidator):
    """ Login Users """
    data = body_user.model_dump()

    """ Checking if e-mail exists in database. """
    finding_email, all_user_informations = AuthService.search_email(data["email"])
    if not finding_email:
        raise NonExistentEmailException()

    """ Validating credentials (Hash). """
    validate_hash = Passwords.verify_password_with_hash(
        data["password"], all_user_informations["password"]
    )
    if not validate_hash:
        raise InvalidCredentialsException()

    return {
        "status": "pending",
        "message": "OTP has been sent to your email. Please confirm to authenticate",
        "email": all_user_informations["email"]
    }

@auth.post("/verify-otp")
async def verify_otp(body: OTPCodeValidator):
    """ Verify OTP - Send with E-mail """

@auth.post("/logout")
async def logout(): pass

@auth.post("/signup", status_code=status.HTTP_201_CREATED)
async def register(body_user: UserCreateValidator):
    """ Register Users """

    """ Organizing the dictionary to send to the service """
    data = body_user.model_dump()
    """ Generate a Unique Identifier """
    data["id"] = UUIDGenerator.generate_identifier()
    data.pop("confirm_password")

    """ Verify Passwords Match """
    match_passwords = Passwords.verify_passwords_match(
        body_user.password,
        body_user.confirm_password
    )
    if not match_passwords:
        raise PasswordsDoNotMatchException()

    """ Checking if e-mail exists in database """
    finding_email, _ = AuthService.search_email(data["email"])
    if finding_email:
        raise DataAlreadyExistsException("E-mail already exists in the database")

    """ Checking if telephone exists in database """
    finding_telephone, _ = AuthService.search_telephone(data["telephone"])
    if finding_telephone:
        raise DataAlreadyExistsException("Telephone already exists in the database")

    """ Encrypting the password """
    data["password"] = Passwords.encrypt_password(data["password"])

    """ Register in the database """
    inserting_user = AuthService.create_user(data)
    return {
        "status": "success",
        "message": "User created successfully",
        "data": inserting_user
    }
