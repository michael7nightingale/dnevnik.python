from fastapi import Request, HTTPException

from app.api.permissions.users import is_teacher_permission
from app.models import Mark, Lesson, StudyGroupSubject


@is_teacher_permission
async def get_mark(request: Request, mark_id: str) -> Mark:
    mark = await Mark.get_or_none(id=mark_id, lesson__study_group_subject__teacher=request.user)
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


@is_teacher_permission
async def get_study_group_subject(request: Request, study_group_subject_id: str) -> StudyGroupSubject:
    study_group_subject = await StudyGroupSubject.get_or_none(id=study_group_subject_id)
    if study_group_subject is None:
        raise HTTPException(
            detail="Журнала не существует.",
            status_code=404
        )
    if study_group_subject.teacher_id != request.user.id:
        raise HTTPException(
            detail="Вы не ведете этот урок у класса.",
            status_code=403
        )
    return study_group_subject
