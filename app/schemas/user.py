from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password : str
    
class UserUpdate(BaseModel):
    username : str | None = None
    password : str | None = None