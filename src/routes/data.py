from fastapi import FastAPI, APIRouter
from fastapi import UploadFile, status
from fastapi.responses import JSONResponse
from fastapi import Depends
import os
from models import ResponseSignal
from helpers.config import get_settings, settings
from controllers.DataController   import DataController  
from controllers import ProjectController
from controllers.ProcessController import ProcessController
import aiofiles
import logging
from .schemes.data import ProcessRequest


logger = logging.getLogger('unicorn.error')

data_router = APIRouter(prefix="/api/v1/data", tags=["/api/v1", "data"])

@data_router.post("/upload/{project_id}") #end point UPLOAD
async def upload_data(
    project_id: str, file: UploadFile,
    app_settings = Depends(get_settings)
    ):

    data_controller = DataController()
    #validate our data => controller file to CONTROL the data : then I'll come here to write the cube data shape
    
    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse (
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                    "signal": result_signal
                    }
        )

    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path, file_id = data_controller.generate_unique_filepath(
        original_filename=file.filename,
          project_id=project_id
          )
    

    try:

        async with aiofiles.open(file_path, "wb") as f:
            while chunck := await file.read(app_settings.FILE_DEFAULT_CHUNCK_SIZE):
                await f.write(chunck)
    except Exception as e:
        logger.error(f"Error while file uploading: {e}")
        return JSONResponse (
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                    "signal": ResponseSignal.FILE_UPLOADED_FAILED.value
                    }
        )


    return JSONResponse (
            content={
                    "signal": ResponseSignal.FILE_UPLOADED_SUCCESS.value,
                    "file_id": file_id
                    }
        )        


# -------------------------------NEXT endpoint -validate the file- ---------------------------------------------
@data_router.post("/process/{project_id}")
async def process_endpoint(project_id: str, process_request : ProcessRequest ): #process req type is ProcessRequest(BaseModel)

    file_id = process_request.file_id
    chunk_size =process_request.chunk_size
    overlab_size = process_request.overlab_size

    process_controller = ProcessController(project_id=project_id)
    file_content = process_controller.get_file_content(file_id=file_id)
    file_chunks=process_controller.process_file_content(
        file_content=file_content,
        file_id=file_id,
        chunk_size=chunk_size,
        overlab_size=overlab_size

    )


    if file_chunks is None or len(file_chunks)==0:
        return JSONResponse (
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                    "signal": ResponseSignal.PROCESSING_FAILED.value
                    }
        )
    
    return file_chunks

