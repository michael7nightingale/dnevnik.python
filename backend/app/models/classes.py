from tortoise import fields
from tortoise.queryset import QuerySetSingle

from .base import TortoiseModel


class Class(TortoiseModel):
    school = fields.ForeignKeyField("models.School", "classes")
    label = fields.CharField(max_length=100)


class Subclass(TortoiseModel):
    label = fields.CharField(max_length=100)
    class_ = fields.ForeignKeyField("models.Class", "subclasses")


class StudyGroup(TortoiseModel):
    class_ = fields.OneToOneField("models.Class", null=True)
    subclass = fields.OneToOneField("models.Subclass", null=True)
    may_join = fields.BooleanField(default=False)
    main_teacher = fields.OneToOneField("models.Teacher", "main_class")

    @classmethod
    def get_or_none(cls, *args, **kwargs) -> QuerySetSingle["StudyGroup"]:
        return (
            super()
            .get_or_none(*args, **kwargs)
            .select_related("class_", "subclass", "subclass__class_", "main_teacher", "main_teacher__user")
        )
