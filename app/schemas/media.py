from pydantic import BaseModel


class MediaCreate(BaseModel):
    title: str
    watched: bool
    genre: str


class MediaUpdate(BaseModel):
    title: str | None = None
    watched: bool | None = None
    genre: str | None = None
