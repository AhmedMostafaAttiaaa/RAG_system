from pydantic import BaseModel, Field, validator
from bson.objectid import ObjectId
from typing import Optional

class Project(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")

    project_id: str = Field(..., min_length=1)

    @validator('project_id')
    def validate_project_id(cls, value):
        if not value.isalnum():
            raise ValueError('project_id must be alphanumeric')
        return value

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

        
    @classmethod            # static method not an inheritied function
    def get_indexes(cls):

        return [
            {
                "key": [
                    ("project_id", 1)
                ],
                "name": "project_id_index_1",
                "unique": True
            }
        ]
