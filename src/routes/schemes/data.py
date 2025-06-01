from pydantic import BaseModel
from typing import Optional

class ProcessRequest(BaseModel): #for the file.. name,chunks..etc
    file_id: str
    chunk_size: Optional[int]=100 #if the user didn't enter an input === make it 100 (defult_)
    overlab_size : Optional[int]=20 #the overlab for chunk to make a contextual between A CHUNK and the previos/next chuck. 
    do_reset: Optional[int]=0