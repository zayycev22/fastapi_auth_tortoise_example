from fastapi import Depends
from fastapi_auth.backends.base import BaseBackend
from fastapi_auth.strategies import DbStrategy
from fastapi_auth.strategies.base import Strategy
from fastapi_auth.tortoise_models import UserRepository

from auth.models import User, get_user_repository, get_db_strategy


class AuthBackend(BaseBackend[User, UserRepository]):
    def __init__(self, user_repo: UserRepository,
                 strategy: Strategy[User, UserRepository]):
        super().__init__(user_repo, strategy)


async def get_backend(user_repo: UserRepository = Depends(get_user_repository),
                      strategy: DbStrategy = Depends(get_db_strategy)):
    yield AuthBackend(user_repo, strategy)
