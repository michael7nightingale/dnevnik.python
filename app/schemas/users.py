from pydantic import BaseModel, EmailStr
from typing import Any

from app.models.users import UserTypesEnum


class UserRole(BaseModel):
    id: str
    name: str


class BaseUserSchema(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    father_name: str
    username: str
    type: UserTypesEnum


class UserSchema(BaseUserSchema):
    id: str


class TypedUserSchema(BaseModel):
    id: str
    user: UserSchema


class LoginUserSchema(BaseModel):
    login: str
    username: str | None = None
    password: str
    email: EmailStr | None = None

    def model_post_init(self, __context: Any) -> None:
        if "@" in self.login:
            self.email = self.login
        else:
            self.username = self.login


class RegisterUserSchema(BaseUserSchema):
    password: str


class UpdateUserSchema(BaseModel):
    email: EmailStr | None = None
    first_name: str
    last_name: str
    father_name: str
    password: str | None = None


class TeacherSchema(BaseModel):
    user: UserSchema


class PupilSchema(BaseUserSchema):
    user: UserSchema
