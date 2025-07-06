import asyncio
from contextlib import asynccontextmanager
from typing import Annotated

from tortoise import Tortoise
from tortoise.exceptions import DoesNotExist

from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import RedirectResponse

from routers.__init__ import core_router
from db import Admin

security = HTTPBasic()
app = FastAPI(title='EMITMAN RANEPA')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(core_router, prefix='/api/v1', tags=['core'])


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'db': ['db']}
    )
    await Tortoise.generate_schemas()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init()
    yield
    await Tortoise.close_connections()


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(
    request: Request,
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    username = credentials.username
    password = credentials.password

    try:
        user = await Admin.get(username=username, password=password)
    except DoesNotExist(Admin):
        return RedirectResponse(url="/")

    if user is not None:
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url
        )

    return RedirectResponse(url="/")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
