from pydantic import BaseModel
from datetime import datetime

from app.models.users import UserTypesEnum


class Token(BaseModel):
    exp: datetime
    user_id: str
    type: UserTypesEnum
