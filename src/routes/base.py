from fastapi import FastAPI, APIRouter
from fastapi import Depends
from dotenv import load_dotenv
load_dotenv(".env")
from helpers.config import get_settings, settings
import os 

           


base_router = APIRouter(prefix="/api/v1", tags=["/api/v1"])

@base_router.get("/")
async def welcome(app_settings = Depends(get_settings)):
    # app_settings = get_settings()
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {
        "app_name": app_name,
        "app_version": app_version,
    }