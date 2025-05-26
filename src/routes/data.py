from fastapi import FastAPI, APIRouter
from fastapi import UploadFile, status
from fastapi.responses import JSONResponse
from fastapi import Depends
import os
from helpers.config import get_settings, settings
from controllers.DataController   import DataController    

data_router = APIRouter(prefix="/api/v1/data", tags=["/api/v1", "data"])

@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str, file: UploadFile,
    app_settings = Depends(get_settings)
    ):
    #validate our data => controller file to CONTROL the data : then I'll come here to write the cube data shape

    is_valid, result_signal = DataController().validate_uploaded_file(file=file)

    return {
        "signal": result_signal
    }


    # if not is_valid:
    #     return JSONResponse (
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         content={
    #                 "signal": result_signal
    #                 }
    #     )

