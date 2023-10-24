from fastapi import APIRouter, Request, Query, Body, Depends
from fastapi.responses import JSONResponse
import datetime

from app.schemas.lessons import (
    LessonUpdateScheme, LessonFullScheme,
    MarkFullScheme, MarkCreateScheme, MarkUpdateScheme,
    StudyGroupSubjectScheme, StudyGroupSubjectDetailScheme, StudyGroupSubjectListScheme,

)
from app.api.permissions.users import is_pupil_permission, is_teacher_permission
from app.api.dependencies.lessons import get_mark, get_lesson, get_study_group_subject
from app.models import Mark, Lesson, StudyGroupSubject, Pupil


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


@router.get("/teacher/lessons")
@is_teacher_permission
async def get_my_lessons_teacher(
        request: Request,
        from_date: datetime.date | None = Query(required=False, default=None),
        to_date: datetime.date | None = Query(required=False, default=None)
):
    return await request.user.get_lessons(from_date, to_date)


@router.get("/teacher/classes/all", response_model=list[StudyGroupSubjectListScheme])
@is_teacher_permission
async def get_teaching_classes(request: Request):
    return [
        {
            **cl.as_dict(),
            "study_group": {
                **cl.study_group.as_dict(),
                "class_": cl.study_group.class_.as_dict() if cl.study_group.class_ is not None else None,
                "subclass": cl.study_group.subclass.as_dict() if cl.study_group.subclass is not None else None
            },
            "subject": cl.subject
        }
        for cl in await request.user.get_teaching_classes()
    ]


@router.get("/teacher/classes/detail/{study_group_subject_id}", response_model=StudyGroupSubjectDetailScheme)
@is_teacher_permission
async def get_teaching_class_detail(
    request: Request,
    study_group_subject: StudyGroupSubject = Depends(get_study_group_subject)
):
    lessons = await Lesson.get_by_study_group_subject(study_group_subject)
    marks = []
    for lesson in lessons:
        marks.extend(lesson.marks)
    return {
        **study_group_subject.as_dict(),
        "study_group": {
            **study_group_subject.study_group.as_dict(),
            "class_": study_group_subject.study_group.class_.as_dict() if study_group_subject.study_group.class_ is not None else None,
            "subclass": study_group_subject.study_group.subclass.as_dict() if study_group_subject.study_group.subclass is not None else None
        },
        "subject": study_group_subject.subject,
        "lessons": lessons,
        "marks": marks,
        "pupils": await Pupil.filter(study_group=study_group_subject.study_group_id)
    }


@router.get("/teacher/lessons/{lesson_id}")
@is_teacher_permission
async def get_lesson_detail(
        request: Request,
        lesson: Lesson = Depends(get_lesson),
):
    return lesson


@router.patch("/teacher/lessons/{lesson_id}")
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
    if not Lesson.filter(study_group_subject__teacher=request.user).exists():
        return JSONResponse(
            {"detail": "Вы не ведете этот урок у данного класса."},
            status_code=400
        )
    return await Mark.create(**mark_data.model_dump())


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
