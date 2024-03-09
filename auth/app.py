from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from auth.backend import AuthBackend, get_backend
from auth.models import User
from auth.schemas import UserData
from fastapi_auth.permissions import IsAuthenticated

from auth.serializers import UserSerializer

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/login")
async def auth(user_data: UserData, backend: AuthBackend = Depends(get_backend)) -> JSONResponse:
    user = await backend.authenticate(email=user_data.email, password=user_data.password)
    if user is None:
        return JSONResponse({"status": "Error", "detail": "Invalid login or password"})
    token = await backend.get_token_by_user(user)
    return JSONResponse({"status": "OK", "token": token})


@auth_router.get("/me", dependencies=[Depends(IsAuthenticated())], response_model=UserSerializer.response_schema())
async def me(request: Request):
    user: User = request.user
    serializer = UserSerializer(user)
    return await serializer.data
