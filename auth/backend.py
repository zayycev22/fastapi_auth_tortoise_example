from fastapi import Depends
from fastapi_auth.backends import Backend
from fastapi_auth.strategies import DbStrategy
from fastapi_auth.tortoise_models import UserRepository
from auth.models import User, get_user_repository, get_db_strategy


async def get_backend(user_repo: UserRepository = Depends(get_user_repository),
                      strategy: DbStrategy = Depends(get_db_strategy)):
    yield Backend[User, UserRepository](user_repo, strategy)
