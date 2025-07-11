from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Literal
from zoneinfo import ZoneInfo

class UserCreateValidator(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    telephone: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("America/Sao_Paulo")))
    password: str
    confirm_password: str

class UserLoginValidator(BaseModel):
    email: EmailStr
    password: str

class OTPCodeValidator(BaseModel):
    otp_code: int

class OTPTypeValidator(BaseModel):
    otp_type: Literal["email", "sms"]