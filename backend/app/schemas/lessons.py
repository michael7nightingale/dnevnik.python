from pydantic import BaseModel, Field
import datetime

from app.schemas.classes import StudyGroupListScheme
from app.schemas.users import TeacherScheme, PupilScheme


class BaseSubjectScheme(BaseModel):
    name: str


class SubjectCreateScheme(BaseSubjectScheme):
    pass


class SubjectScheme(BaseSubjectScheme):
    id: str


class BaseStudyGroupSubjectScheme(BaseModel):
    subject: SubjectScheme
    teacher_id: str
    study_group_id: str


class StudyGroupSubjectScheme(BaseStudyGroupSubjectScheme):
    id: str
    teacher: TeacherScheme


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
    mark: str
    is_ill: bool = Field(default=False)
    is_absent: bool = Field(default=False)
    is_skipped: bool = Field(default=False)


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


class MarkListScheme(BaseMarkScheme):
    id: str


class MarkUpdateScheme(BaseModel):
    mark: str | None = Field(default=None, max_length=1)
    is_ill: bool | None = None
    is_absent: bool | None = None
    is_skipped: bool | None = None

    def model_post_init(self, __context) -> None:
        if not self.mark.isnumeric():
            match self.mark.upper():
                case "Н":
                    self.is_skipped = True
                case "У":
                    self.is_absent = True
                case "Б":
                    self.is_ill = True
            self.mark = self.mark.upper()


class StudyGroupSubjectListScheme(BaseStudyGroupSubjectScheme):
    id: str
    study_group: StudyGroupListScheme
    subject: SubjectScheme


class StudyGroupSubjectDetailScheme(BaseStudyGroupSubjectScheme):
    id: str
    study_group: StudyGroupListScheme
    pupils: list[PupilScheme]
    subject: SubjectScheme
    lessons: list[LessonScheme]
    marks: list[MarkListScheme]
