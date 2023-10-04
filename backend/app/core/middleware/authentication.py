from starlette.middleware import authentication
from starlette.requests import HTTPConnection

from app.models.users import get_typed_user
from app.services.jwt import decode_jwt_token


class AuthenticationBackend(authentication.AuthenticationBackend):

    async def verify_token(self, token: str):
        scopes = []
        if token is None:
            return scopes, None

        token = token.split()[-1]
        token_data = decode_jwt_token(token)
        if token_data is None:
            return scopes, None
        user = await get_typed_user(type=token_data.type, user_id=token_data.user_id)
        return scopes, user

    def get_token(self, conn: HTTPConnection) -> str | None:
        token = conn.headers.get("authorization")
        return token

    async def authenticate(self, conn: HTTPConnection):
        token = self.get_token(conn)
        response = await self.verify_token(token)
        scopes, user = response
        return authentication.AuthCredentials(scopes=scopes), user
