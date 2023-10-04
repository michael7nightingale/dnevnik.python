from functools import wraps
from fastapi import Request, HTTPException

from app.models import Pupil, Teacher, Administrator


def login_required(func):
    """Login required decorator to wrap view."""
    @wraps(func)
    async def inner(request: Request, *args, **kwargs):
        if request.user is None:
            raise HTTPException(
                detail="Authentication required.",
                status_code=403
            )
        response = await func(request, *args, **kwargs)
        return response
    return inner


def is_teacher_permission(func):
    @wraps(func)
    @login_required
    async def inner(request: Request, *args, **kwargs):
        if not isinstance(request.user, Teacher):
            raise HTTPException(
                detail="Вы не учитель.",
                status_code=403
            )
        response = await func(request, *args, **kwargs)
        return response
    return inner


def is_pupil_permission(func):
    @wraps(func)
    @login_required
    async def inner(request: Request, *args, **kwargs):
        if not isinstance(request.user, Pupil):
            raise HTTPException(
                detail="Вы не ученик.",
                status_code=403
            )
        response = await func(request, *args, **kwargs)
        return response
    return inner


def is_administrator_permission(func):
    @wraps(func)
    @login_required
    async def inner(request: Request, *args, **kwargs):
        if not isinstance(request.user, Administrator):
            raise HTTPException(
                detail="Вы не администратор.",
                status_code=403
            )
        response = await func(request, *args, **kwargs)
        return response
    return inner
