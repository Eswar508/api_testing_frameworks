from fastapi import FastAPI
from fastapi.responses import JSONResponse
from FastApi.routes.admin import app as admin_router
from FastApi.routes.students import app as students_router
from FastApi.routes.authentication import app as auth_router
from FastApi.utils.helper_fun import APIException
app=FastAPI()
app.include_router(admin_router)
app.include_router(students_router)
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message":"welcome to fast api"}
@app.exception_handler(APIException)
async def custom_api_exception(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.message
        }
    )