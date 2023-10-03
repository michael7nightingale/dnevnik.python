from functools import wraps
from fastapi import Request, HTTPException

from .users import login_required


def is_in_class_permission(func):
    @wraps(func)
    @login_required
    async def inner(request: Request, *args, **kwargs):
        if request.user.type != "teacher":
            raise HTTPException(
                detail="Вы не учитель.",
                status_code=403
            )
        response = await func(request, *args, **kwargs)
        return response
    return inner
