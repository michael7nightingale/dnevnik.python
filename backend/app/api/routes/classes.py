from fastapi import APIRouter, Request

from app.models import StudyGroup, Pupil
from app.schemas.classes import StudyGroupScheme
from app.api.permissions.users import is_pupil_or_teacher_permission


router = APIRouter(prefix="/classes")


@router.get("/my-class", response_model=StudyGroupScheme)
@is_pupil_or_teacher_permission
async def get_my_class(request: Request):
    """Endpoint for getting leaded class or studying class."""
    study_group = await request.user.get_study_group()
    return {
        **study_group.as_dict(),
        "class_": study_group.class_,
        "subclass": study_group.subclass,
        "main_teacher": study_group.main_teacher,
        "pupils": await Pupil.all_by_study_group(study_group)
    }
