from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from app.config import settings
from app.exception import SQLAlchemyErrorException
from app.users import users_routers

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
)


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.exception_handler(SQLAlchemyErrorException)
async def sql_alchemy_exception(request, exc: SQLAlchemyErrorException):
    raise HTTPException(
        status_code=400,
        detail=exc.detail
    )


app.include_router(users_routers)
