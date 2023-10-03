from pydantic import BaseModel, EmailStr
from typing import Any

from app.models.users import UserTypesEnum


class UserRole(BaseModel):
    id: str
    name: str


class BaseUserScheme(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    father_name: str
    username: str
    type: UserTypesEnum


class UserScheme(BaseUserScheme):
    id: str


class TypedUserScheme(BaseModel):
    id: str
    user: UserScheme


class LoginUserScheme(BaseModel):
    login: str
    username: str | None = None
    password: str
    email: EmailStr | None = None

    def model_post_init(self, __context: Any) -> None:
        if "@" in self.login:
            self.email = self.login
        else:
            self.username = self.login


class RegisterUserScheme(BaseUserScheme):
    password: str


class UpdateUserScheme(BaseModel):
    email: EmailStr | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    father_name: str | None = None


class TeacherScheme(BaseModel):
    user: UserScheme


class PupilScheme(BaseModel):
    id: str
    user: UserScheme
