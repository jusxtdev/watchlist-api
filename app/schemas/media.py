from pydantic import BaseModel
from datetime import datetime

class MediaCreate(BaseModel):
    title: str
    watched: bool
    genre: str


class MediaUpdate(BaseModel):
    title: str | None = None
    watched: bool | None = None
    genre: str | None = None

class MediaResponse(BaseModel):
    id : int
    title : str
    watched : bool
    genre : str
    created_at : datetime
    updated_at : datetime