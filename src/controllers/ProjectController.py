# this file to save my uploaded file into assets>>files

from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal

class ProjectController(BaseController):

    def __init__(self):
        super().__init__()