from tortoise import fields

from .base import TortoiseModel


class Lesson(TortoiseModel):
    date = fields.DateField()
    start_at = fields.TimeField()
    finish_at = fields.TimeField()
    study_group = fields.ForeignKeyField("models.StudyGroup", "lessons")
    teacher = fields.ForeignKeyField("models.Teacher", "lessons")
    science = fields.CharField(max_length=255)
    theme = fields.CharField(max_length=255)
    homework = fields.TextField(null=True)

    @classmethod
    async def filter(cls, *args, **kwargs) -> list["Lesson"]:
        return await (
            super()
            .filter(*args, **kwargs)
            .select_related("teacher")
        )


class Mark(TortoiseModel):
    lesson = fields.ForeignKeyField("models.Lesson")
    pupil = fields.ForeignKeyField("models.Pupil")
    mark = fields.SmallIntField(null=True)
    is_ill = fields.BooleanField(default=False)
    is_absent = fields.BooleanField(default=False)
    is_skipped = fields.BooleanField(default=False)

    @classmethod
    async def filter(cls, *args, **kwargs) -> list["Mark"]:
        return await (
            super()
            .filter(*args, **kwargs)
            .select_related("lesson")
        )
