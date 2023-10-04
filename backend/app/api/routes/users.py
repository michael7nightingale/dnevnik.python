from fastapi import APIRouter, Body, Request
from fastapi.responses import JSONResponse

from app.schemas.users import UpdateUserScheme, LoginUserScheme, RegisterUserScheme, TypedUserScheme
from app.models.users import User, create_typed_user
from app.services.jwt import encode_jwt_token
from app.api.permissions.users import login_required


router = APIRouter(prefix="/auth")


@router.post("/register", response_model=TypedUserScheme)
async def register(register_data: RegisterUserScheme = Body()):
    """User register endpoint."""
    new_user = await create_typed_user(**register_data.model_dump())
    if new_user is None:
        return JSONResponse(
            content={
                "detail": "User with such data already exists.",
            },
            status_code=400
        )
    return new_user


@router.post("/token")
async def token_login(login_data: LoginUserScheme = Body()):
    """User login (getting access token) endpoint."""
    user = await User.login(**login_data.model_dump(include={"username", "password", "email"}))
    if user is None:
        return JSONResponse(
            content={
                "detail": "Auth credentials are invalid.",
            },
            status_code=400
        )
    return {"access-token": encode_jwt_token(type=user.type, user_id=user.id)}


@router.get("/me", response_model=TypedUserScheme)
@login_required
async def me_profile(request: Request):
    """Getting current user data endpoint."""
    return request.user


@router.patch("/me", response_model=TypedUserScheme)
@login_required
async def me_update(request: Request, update_data: UpdateUserScheme):
    """Getting current user data endpoint."""
    await request.user.user.update_from_dict(update_data.model_dump())
    return request.user
