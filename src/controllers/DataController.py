from fastapi import UploadFile
# Here they will inhirite from BaseController File in Controllers
from .BaseController import BaseController
from models import ResponseSignal
from .ProjectController import ProjectController
import regex as re
import os

# ----------------------------------------

class DataController(BaseController):
    def __init__(self):
        super().__init__() # to call the init of super === which is BaseController
        self.size_scale = 1048576 # to convert MBs to bytes -> because file.size is dealing with bytes not MEGABYTES


    def validate_uploaded_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_EXTINTIONS:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value

        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value

        return True, ResponseSignal.FILE_UPLOADED_SUCCESS.value
    
    def generate_unique_filepath(self, original_filename: str, project_id: str):

        random_filename = self.generate_random_string()
        project_path =ProjectController().get_project_path(project_id=project_id)

        cleaned_file_name = self.get_clean_file_name(original_filename=original_filename)

        new_file_path = os.path.join(

            project_path,
            random_filename + "__" + cleaned_file_name
        )

        while os.path.exists(new_file_path):
            random_filename= self.generate_random_string()
            new_file_path = os.path.join(
                project_path,
                random_filename + "__" + cleaned_file_name
            )

        return new_file_path, random_filename + "__" + cleaned_file_name


    def get_clean_file_name (self, original_filename: str):

            cleaned_file_name = re.sub(r'[^\w.]', '', original_filename.strip())
            cleaned_file_name = cleaned_file_name.replace(" ","_")

            return cleaned_file_name