from fastapi import Depends
from fastapi_auth.tortoise_models import Token, EmailUser, UserRepository, TokenRepository
from fastapi_auth.strategies import DbStrategy


class User(EmailUser):
    class Meta:
        table = "user"


class AccessToken(Token):
    class Meta:
        table = "token"


async def get_user_repository():
    yield UserRepository(User)


async def get_token_repository():
    yield TokenRepository(AccessToken)


async def get_db_strategy(
        user_repo: UserRepository = Depends(get_user_repository),
        token_repo: TokenRepository = Depends(get_token_repository)
) -> DbStrategy:
    yield DbStrategy(user_repo=user_repo, token_repo=token_repo)
