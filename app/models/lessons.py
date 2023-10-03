from tortoise import fields

from .base import TortoiseModel


class StudyWeek(TortoiseModel):
    pass


class StudyDay(TortoiseModel):
    day = fields.CharField(max_length=20)
    study_week = fields.ForeignKeyField("models.StudyWeek", "study_days")
    is_weekend = fields.BooleanField(default=False)


class Lesson(TortoiseModel):
    start_at = fields.TimeField()
    finish_at = fields.TimeField()
    study_group = fields.ForeignKeyField("models.StudyGroup", "lessons")
    teacher = fields.ForeignKeyField("models.Teacher", "lessons")
    science = fields.CharField(max_length=255)
    theme = fields.CharField(max_length=255)
    homework = fields.TextField(null=True)


class Mark(TortoiseModel):
    lesson = fields.ForeignKeyField("models.Lesson")
    pupil = fields.ForeignKeyField("models.Pupil")
    mark = fields.SmallIntField(null=True)
    is_ill = fields.BooleanField(default=False)
    is_absent = fields.BooleanField(default=False)
    is_skipped = fields.BooleanField(default=False)
