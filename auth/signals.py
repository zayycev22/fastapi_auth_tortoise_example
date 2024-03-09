from fastapi_auth.signals import Signal

from auth.models import User, AccessToken

signal = Signal()


@signal.after_save(model=User)
async def create_token(instance: User, created: bool):
    if created:
        await AccessToken.create(user=instance)
