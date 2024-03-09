from fastapi import Depends
from fastapi_auth.managers.base import BaseUserManager
from fastapi_auth_tortoise_models import UserRepository

from auth.models import User, get_user_repository


class UserManager(BaseUserManager[User, UserRepository]):
    ...


async def get_user_manager(user_repo: UserRepository = Depends(get_user_repository)):
    yield UserManager(repo=user_repo)
