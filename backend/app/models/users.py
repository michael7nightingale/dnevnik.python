from tortoise import fields
from tortoise.expressions import Q
from tortoise.exceptions import IntegrityError
from tortoise.queryset import QuerySet, QuerySetSingle
from tortoise.transactions import in_transaction

from uuid import uuid4
import datetime
from enum import StrEnum, auto
import random
from typing import Optional

from .lessons import Lesson, Mark
from .base import TortoiseModel
from .schools import School
from .classes import StudyGroup
from app.services.passwords import verify_password, hash_password


def generate_identifier() -> str:
    return "".join(str(random.randint(0, 9)) for _ in range(8))


def generate_password() -> str:
    psw = str(uuid4()).replace("-", "")
    idx_range = list(range(len(psw)))
    random.shuffle(idx_range)
    return "".join(psw[idx] for idx in idx_range)


class UserRole(TortoiseModel):
    name = fields.CharField(unique=True, max_length=100)


class User(TortoiseModel):
    id = fields.CharField(pk=True, default=generate_identifier, max_length=18)
    first_name = fields.CharField(max_length=100)
    last_name = fields.CharField(max_length=100)
    father_name = fields.CharField(max_length=100)
    email = fields.CharField(unique=True, index=True, max_length=100)
    password = fields.CharField(max_length=255, default=generate_password)
    username = fields.CharField(max_length=255, unique=True, index=True)
    type = fields.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.father_name} {self.first_name} {self.father_name}"

    @classmethod
    async def login(cls, password: str, email: str | None = None, username: str | None = None) -> Optional["User"]:
        if email is None and username is None:
            return None
        if email is not None and username is not None:
            return None
        statements = {"email": email} if email is not None else {"username": username}
        user = await cls.get_or_none(**statements)
        if user is not None:
            if verify_password(password, user.password):
                return user
        return None

    @classmethod
    async def register(
            cls,
            type: str,
            first_name: str,
            last_name: str,
            father_name: str,
            username: str,
            email: str,
            password: str | None = None,
            **kwargs
    ) -> Optional["User"]:
        if password is None:
            password = generate_password()
        try:
            print(first_name, last_name, father_name, username, email, password, type)
            new_user = await cls.create(
                first_name=first_name,
                last_name=last_name,
                father_name=father_name,
                username=username,
                email=email,
                password=hash_password(password),
                type=type
            )
            return new_user
        except IntegrityError:
            return None


class UserTypeModel(TortoiseModel):
    type: str
    user = fields.OneToOneField("models.User")
    school = fields.ForeignKeyField("models.School")
    is_administrator = fields.BooleanField(default=False)

    @classmethod
    async def create(cls, **kwargs) -> Optional["UserTypeModel"]:
        async with in_transaction():
            user = await User.register(type=cls.type, **kwargs)
            if user is None:
                return
            return await super().create(**kwargs, user=user, school=(await School.first()), study_group=(await StudyGroup.first()))    # type: ignore

    @classmethod
    def get_or_none(cls, *args, **kwargs) -> QuerySetSingle[Optional["UserTypeModel"]]:
        return (
            super()
            .get_or_none(*args, **kwargs)
            .select_related("user", "school")
        )

    @classmethod
    def filter(cls, *args, **kwargs) -> QuerySet["UserTypeModel"]:
        return (
            super()
            .filter(*args, **kwargs)
            .select_related("user", "school")
        )

    class Meta:
        abstract = True


class Teacher(UserTypeModel):
    type = "teacher"
    user = fields.OneToOneField("models.User", "teacher")
    school = fields.ForeignKeyField("models.School", "teachers")

    def get_lessons(
            self,
            from_date: datetime.date | None = None,
            to_date: datetime.date | None = None
    ) -> QuerySet[Lesson]:
        if from_date is not None and to_date is not None:
            args = Q(date__gte=from_date) | Q(date__lte=to_date)
        else:
            args = Q(date__gte=from_date) if from_date is not None else Q(date__lte=to_date)
        return Lesson.filter(
            args,
            teacher=self
        )

    async def get_study_group(self) -> StudyGroup | None:
        return await StudyGroup.get_or_none(main_teacher=self)

    async def get_marks(
            self,
            from_date: datetime.date | None = None,
            to_date: datetime.date | None = None
    ) -> list[Mark]:
        if from_date is not None and to_date is not None:
            args = Q(lesson__date__gte=from_date) | Q(lesson__date__lte=to_date)
        else:
            args = Q(lesson__date__gte=from_date) if from_date is not None else Q(lesson__date__lte=to_date)
        return await Mark.filter(
            args,
            teacher=self
        )


class Pupil(UserTypeModel):
    type = "pupil"
    user = fields.OneToOneField("models.User", "pupil")
    school = fields.ForeignKeyField("models.School", "pupils")
    study_group = fields.ForeignKeyField("models.StudyGroup", "pupils")

    async def get_study_group(self) -> StudyGroup:
        return await StudyGroup.get_or_none(id=self.study_group_id)

    async def get_lessons(
            self,
            from_date: datetime.date | None = None,
            to_date: datetime.date | None = None
    ) -> list[Lesson]:
        if from_date is None and to_date is None:
            return await Lesson.filter(study_group_id=self.study_group_id)
        if from_date is not None and to_date is not None:
            args = Q(date__gte=from_date) | Q(date__lte=to_date)
        else:
            args = Q(date__gte=from_date) if from_date is not None else Q(date__lte=to_date)
        return await Lesson.filter(
            args,
            study_group_id=self.study_group_id,
        )

    async def get_marks(
            self,
            from_date: datetime.date | None = None,
            to_date: datetime.date | None = None
    ) -> list[Mark]:
        if from_date is None and to_date is None:
            return await Mark.filter(pupil=self)
        if from_date is not None and to_date is not None:
            args = Q(lesson__date__gte=from_date) | Q(lesson__date__lte=to_date)
        else:
            args = Q(lesson__date__gte=from_date) if from_date is not None else Q(lesson__date__lte=to_date)
        return await Mark.filter(
            args,
            pupil=self,
        )

    @classmethod
    def all_by_study_group(cls, study_group: StudyGroup):
        return (
            super()
            .filter(study_group=study_group)
            .order_by("user__last_name", "user__first_name", "user__father_name")
        )


class UserTypesEnum(StrEnum):
    teacher = auto()
    pupil = auto()
    administrator = auto()


class Administrator(UserTypeModel):
    type = "administrator"
    user = fields.OneToOneField("models.User", "administrator")
    school = fields.ForeignKeyField("models.School", "administrators")
    is_administrator = fields.BooleanField(default=True)


user_types_matching = {
    Pupil.type: Pupil,
    Teacher.type: Teacher,
    Administrator.type: Administrator,

}


async def get_typed_user(type: str, user_id: str) -> UserTypeModel | None:
    model_class = user_types_matching.get(type)
    if model_class is None:
        return
    return await model_class.get_or_none(user_id=user_id)


async def create_typed_user(type: str, **kwargs) -> Optional[UserTypeModel]:
    model_class = user_types_matching.get(type)
    if model_class is None:
        return
    return await model_class.create(**kwargs)
