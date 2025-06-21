from pydantic import BaseModel, EmailStr

class UserCreateValidator(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    telephone: int
    password: str
    confirm_password: str

class UserLoginValidator(BaseModel): pass