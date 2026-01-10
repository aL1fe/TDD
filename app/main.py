from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse

from app.api_exceptions import BaseAPIException
from app.user_service import UserService, get_user_service


app = FastAPI()


@app.exception_handler(BaseAPIException)
def user_not_found_handler(request: Request, exc: BaseAPIException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "error_code": exc.error_code, "extra": exc.extra},
    )


@app.get("/users/{id}")
async def get_user(id: int, user_service: UserService = Depends(get_user_service)):
    return await user_service.get_user_by_id(id)
