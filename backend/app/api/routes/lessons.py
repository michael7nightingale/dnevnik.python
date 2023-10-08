from fastapi import APIRouter, Request, Query, Body, Depends
import datetime

from app.schemas.lessons import (
    LessonUpdateScheme, LessonFullScheme,
    MarkFullScheme, MarkCreateScheme, MarkUpdateScheme,
    StudyGroupSubjectScheme,

)
from app.api.permissions.users import is_pupil_permission, is_teacher_permission
from app.api.dependencies.lessons import get_mark, get_lesson
from app.models import Mark, Lesson


router = APIRouter(prefix="/lessons")


@router.get("/subjects", response_model=list[StudyGroupSubjectScheme])
@is_pupil_permission
async def get_my_lessons(request: Request):
    return await request.user.get_subjects()


@router.get("/", response_model=list[LessonFullScheme])
@is_pupil_permission
async def get_my_lessons(
        request: Request,
        from_date: datetime.date | None = Query(required=False, default=None),
        to_date: datetime.date | None = Query(required=False, default=None)
):
    return await request.user.get_lessons(from_date, to_date)


@router.get("/teacher")
@is_teacher_permission
async def get_my_lessons_teacher(
        request: Request,
        from_date: datetime.date | None = Query(required=False, default=None),
        to_date: datetime.date | None = Query(required=False, default=None)
):
    return await request.user.get_lessons(from_date, to_date)


@router.get("/teacher/{lesson_id}")
@is_teacher_permission
async def get_lesson_detail(
        request: Request,
        lesson: Lesson = Depends(get_lesson),
):
    return lesson


@router.patch("/teacher/{lesson_id}")
@is_teacher_permission
async def update_lesson(
        request: Request,
        lesson: Lesson = Depends(get_lesson),
        lesson_data: LessonUpdateScheme = Body()
):
    await lesson.update_from_dict(lesson_data.model_dump())
    await lesson.save()
    return lesson


@router.get("/marks", response_model=list[MarkFullScheme])
@is_pupil_permission
async def get_my_marks(
        request: Request,
        from_date: datetime.date | None = Query(required=False, default=None),
        to_date: datetime.date | None = Query(required=False, default=None)
):
    return await request.user.get_marks(from_date, to_date)


@router.post("/marks")
@is_teacher_permission
async def create_mark(
        request: Request,
        mark_data: MarkCreateScheme = Body()
):
    return await mark_data.create(**mark_data.model_dump())


@router.patch("/marks/{mark_id}")
@is_teacher_permission
async def update_mark(
        request: Request,
        mark: Mark = Depends(get_mark),
        mark_data: MarkUpdateScheme = Body()
):
    await mark.update_from_dict(mark_data.model_dump())
    await mark.save()
    return mark


@router.delete("/marks/{mark_id}")
@is_teacher_permission
async def delete_mark(
        request: Request,
        mark: Mark = Depends(get_mark),
):
    await mark.delete()
    return {"detail": "Оценка удалена."}
