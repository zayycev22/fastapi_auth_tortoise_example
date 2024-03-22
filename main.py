import uvicorn
from fastapi import FastAPI, Depends, Request
from fastapi.security import APIKeyHeader
from fastapi_auth import FastApiAuth
from fastapi_auth.authenticators import Authenticator
from fastapi_auth.backends import Backend
from tortoise.contrib.fastapi import register_tortoise
from auth.backend import get_backend
from auth.signals import signal
from settings import DATABASE_URL
from auth.router import auth_router
from books.router import book_router

api_key_header = APIKeyHeader(name='Authorization', auto_error=False)
fastapi_auth = FastApiAuth()


async def auth_dependency(backend: Backend = Depends(get_backend)):
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
    modules={"models": ["auth.models", "books.models"]},
    db_url=DATABASE_URL,
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(auth_router, tags=["authentication"])
app.include_router(book_router, tags=["books"])

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
