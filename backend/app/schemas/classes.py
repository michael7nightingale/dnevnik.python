from pydantic import BaseModel, Field

from .users import TeacherScheme, PupilScheme


class ClassScheme(BaseModel):
    label: str


class SubclassScheme(BaseModel):
    label: str
    class_: ClassScheme | None = None


class StudyGroupScheme(BaseModel):
    class_: ClassScheme | None = None
    subclass: SubclassScheme | None = None
    may_join: bool
    main_teacher: TeacherScheme
    pupils: list[PupilScheme]
