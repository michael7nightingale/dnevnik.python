from pydantic import BaseModel
import datetime

from app.schemas.users import TeacherScheme


class BaseLessonScheme(BaseModel):
    date: datetime.date
    science: str
    theme: str


class LessonScheme(BaseLessonScheme):
    id: str


class LessonFullScheme(BaseLessonScheme):
    start_at: datetime.time
    finish_at: datetime.time
    study_group_id: str
    teacher: TeacherScheme
    homework: str


class LessonUpdateScheme(BaseLessonScheme):
    theme: str
    homework: str


class BaseMarkScheme(BaseModel):
    lesson_id: str
    pupil_id: str
    mark: int
    is_ill: bool
    is_absent: bool
    is_skipped: bool


class MarkCreateScheme(BaseMarkScheme):
    pass


class MarkScheme(BaseModel):
    id: str
    lesson: LessonScheme
    mark: int
    is_ill: bool
    is_absent: bool
    is_skipped: bool


class MarkUpdateScheme(BaseModel):
    id: str
    mark: int | None = None
    is_ill: bool | None = None
    is_absent: bool | None = None
    is_skipped: bool | None = None
