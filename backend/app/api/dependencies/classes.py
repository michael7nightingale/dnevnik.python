from fastapi import Request, HTTPException

from app.models import StudyGroup


async def get_class(request: Request, class_id: str) -> StudyGroup:
    study_group = await StudyGroup.get_or_none(id=class_id)
    if study_group is None:
        raise HTTPException(
            detail="Класс не найден",
            status_code=404
        )
    return study_group
