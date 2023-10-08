from pydantic import BaseModel
import datetime

from app.schemas.classes import StudyGroupScheme
from app.schemas.users import TeacherScheme


class BaseSubjectScheme(BaseModel):
    name: str


class SubjectCreateScheme(BaseSubjectScheme):
    pass


class SubjectScheme(BaseSubjectScheme):
    id: str


class BaseStudyGroupSubjectScheme(BaseModel):
    subject: SubjectScheme
    study_group_id: str
    teacher: TeacherScheme


class StudyGroupSubjectScheme(BaseStudyGroupSubjectScheme):
    id: str


class BaseLessonScheme(BaseModel):
    start_at: datetime.time | None = None
    date: datetime.date | None = None
    finish_at: datetime.time | None = None
    theme: str
    homework: str | None = None
    study_group_subject_id: str


class LessonScheme(BaseLessonScheme):
    id: str


class LessonFullScheme(BaseLessonScheme):
    study_group_subject: StudyGroupSubjectScheme


class LessonCreateScheme(BaseLessonScheme):
    study_group_id: str


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


class MarkFullScheme(BaseMarkScheme):
    lesson: LessonScheme


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
