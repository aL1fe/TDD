from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse

from app.exceptions import UserNotFoundError
from app.user_service import UserService, get_user_service


app = FastAPI()


@app.exception_handler(UserNotFoundError)
def user_not_found_handler(request: Request, exc: UserNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": exc.message},
    )


@app.get("/users/{id}")
async def get_user(id: int, user_service: UserService = Depends(get_user_service)):
    return await user_service.get_user_by_id(id)
