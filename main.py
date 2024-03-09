import uvicorn
from fastapi import FastAPI, Depends, Request
from fastapi.security import APIKeyHeader
from fastapi_auth import FastApiAuth
from fastapi_auth.authenticators import Authenticator
from tortoise.contrib.fastapi import register_tortoise
from auth.backend import AuthBackend, get_backend
from auth.signals import signal
from settings import DATABASE_URL
from auth.app import auth_router

api_key_header = APIKeyHeader(name='Authorization', auto_error=False)
fastapi_auth = FastApiAuth()


async def auth_dependency(backend: AuthBackend = Depends(get_backend)):
    yield Authenticator(backend=backend)


async def process_token(request: Request, token=Depends(api_key_header),
                        authenticator: Authenticator = Depends(auth_dependency)):
    await authenticator.process_token(request=request, raw_token=token)


app = FastAPI(dependencies=[Depends(process_token)])


@app.on_event("startup")
async def startup():
    fastapi_auth.listen_signals(signal)

register_tortoise(
    app,
    modules={"models": ["auth.models"]},
    db_url=DATABASE_URL,
    add_exception_handlers=True,
)

app.include_router(auth_router, tags=["authentication"])


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
