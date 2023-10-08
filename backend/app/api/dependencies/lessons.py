from fastapi import Request, HTTPException

from app.api.permissions.users import is_teacher_permission
from app.models import Mark, Lesson


@is_teacher_permission
async def get_mark(request: Request, mark_id: str) -> Mark:
    mark = await Mark.get_or_none(id=mark_id, lesson__teacher=request.user)
    if mark is None:
        raise HTTPException(
            detail="Оценки не существует.",
            status_code=404
        )
    return mark


@is_teacher_permission
async def get_lesson(request: Request, lesson_id: str) -> Lesson:
    lesson = await Lesson.get_or_none(id=lesson_id, teacher=request.user)
    if lesson is None:
        raise HTTPException(
            detail="Урока не существует.",
            status_code=404
        )
    return lesson
