from fastapi import APIRouter, Request

from app.models import StudyGroup, Pupil
from app.schemas.classes import StudyGroupScheme
from app.api.permissions.users import is_pupil_permission


router = APIRouter(prefix="/classes")


@router.get("/my-class", response_model=StudyGroupScheme)
@is_pupil_permission
async def get_my_class(request: Request):
    study_group = await request.user.get_study_group()
    return {
        **study_group.as_dict(),
        "class_": study_group.class_,
        "subclass": study_group.subclass,
        "main_teacher": study_group.main_teacher,
        "pupils": await Pupil.filter(study_group=study_group)
    }
