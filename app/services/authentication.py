from functools import wraps
from fastapi import Request, HTTPException


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
