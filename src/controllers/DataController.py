from fastapi import UploadFile
# Here they will inhirite from BaseController File in Controllers
from .BaseController import BaseController
from models import ResponseSignal

class DataController(BaseController):
    def __init__(self):
        super().__init__() #to call the init of super === which is BaseController
        self.size_scale = 1048576 # to convert MBs to bytes -> because file.size is dealing with bytes not MEGABYTES


    def validate_uploaded_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_EXTINTIONS:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value

        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value

        return True, ResponseSignal.FILE_UPLOADED_SUCCESS.value