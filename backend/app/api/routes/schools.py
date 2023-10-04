from fastapi import APIRouter, Request

from app.api.permissions.users import login_required
from app.schemas.schools import SchoolScheme


router = APIRouter(prefix="/schools")


@router.get("/my-school", response_model=SchoolScheme)
@login_required
async def get_user_school(request: Request):
    return request.user.school
