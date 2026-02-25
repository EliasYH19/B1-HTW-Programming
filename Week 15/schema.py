from pydantic import BaseModel

# Model for creating a new user 
class UserCreate(BaseModel):
    name: str
    email: str

# Model representing a user with an ID
class User(BaseModel):
    id: int
    name: str

    email: str
