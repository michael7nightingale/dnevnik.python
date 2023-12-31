from tortoise import fields
from tortoise.queryset import QuerySet, QuerySetSingle
import datetime

from .base import TortoiseModel


class Subject(TortoiseModel):
    name = fields.CharField(max_length=255)


class StudyGroupSubject(TortoiseModel):
    subject = fields.ForeignKeyField("models.Subject")
    teacher = fields.ForeignKeyField("models.Teacher")
    study_group = fields.ForeignKeyField("models.StudyGroup")

    @classmethod
    def filter(cls, *args, **kwargs) -> QuerySet["StudyGroupSubject"]:
        return (
            super()
            .filter(*args, **kwargs)
            .select_related("subject", "study_group",  "study_group__class_", "study_group__subclass")
        )

    @classmethod
    def get_or_none(cls, *args, **kwargs) -> QuerySetSingle["StudyGroupSubject"] | None:
        return (
            super()
            .get_or_none(*args, **kwargs)
            .select_related("subject", "study_group", "study_group__class_", "study_group__subclass")
        )

    class Meta:
        unique_together = [("subject", "teacher", "study_group")]


class Lesson(TortoiseModel):
    date = fields.DateField(default=lambda: datetime.datetime.now().date(), null=True)
    start_at = fields.TimeField(default=lambda: datetime.datetime.now().time(), null=True)
    finish_at = fields.TimeField(default=lambda: datetime.datetime.now().time(), null=True)
    place = fields.CharField(max_length=40)
    study_group_subject = fields.ForeignKeyField("models.StudyGroupSubject", related_name="lessons")
    theme = fields.CharField(max_length=255)
    homework = fields.TextField(null=True)

    @classmethod
    def filter(cls, *args, **kwargs) -> QuerySet["Lesson"]:
        return (
            super()
            .filter(*args, **kwargs)
            .select_related(
                "study_group_subject", "study_group_subject__subject",
                "study_group_subject__teacher", "study_group_subject__teacher__user")
        )

    @classmethod
    async def get_by_study_group_subject(cls, study_group_subject: StudyGroupSubject) -> list["Lesson"]:
        return await (
            super()
            .filter(study_group_subject=study_group_subject)
            .prefetch_related("marks")
        )


class Mark(TortoiseModel):
    lesson = fields.ForeignKeyField("models.Lesson", related_name="marks")
    pupil = fields.ForeignKeyField("models.Pupil", related_name="pupils")
    mark = fields.CharField(null=True, max_length=1)
    is_ill = fields.BooleanField(default=False)
    is_absent = fields.BooleanField(default=False)
    is_skipped = fields.BooleanField(default=False)

    @classmethod
    def filter(cls, *args, **kwargs) -> QuerySet["Mark"]:
        return (
            super()
            .filter(*args, **kwargs)
            .select_related("lesson")
        )
