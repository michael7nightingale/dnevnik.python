from fastapi import APIRouter, Request, Depends

from app.api.dependencies.classes import get_class
from app.models import StudyGroup, Pupil
from app.schemas.classes import StudyGroupScheme
from app.api.permissions.users import is_pupil_or_teacher_permission, login_required


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


@router.get("/detail/{class_id}")
@login_required
async def get_class_detail(
        request: Request,
        study_group: StudyGroup = Depends(get_class)
):
    return {
        **study_group.as_dict(),
        "class_": study_group.class_,
        "subclass": study_group.subclass,
        "main_teacher": study_group.main_teacher,
        "pupils": await Pupil.all_by_study_group(study_group)
    }
