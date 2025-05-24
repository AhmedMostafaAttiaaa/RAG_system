from fastapi import FastAPI, APIRouter
# from dotenv import load_dotenv
# load_dotenv(".env") # moved to main

import os 
            

base_router = APIRouter(
    prefix="/api/v1",
    tags=["/api/v1"]
)


@base_router.get("/")
async def welcome():
    app_name = os.getenv('APP_NAME') 
    app_version = os.getenv('APP_VERSION') 
    return {
        "app_name": app_name,
        "app_version": app_version,
    }



