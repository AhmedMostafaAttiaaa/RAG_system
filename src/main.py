from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv(".env")  

from routes import base  

app = FastAPI()

app.include_router(base.base_router)



