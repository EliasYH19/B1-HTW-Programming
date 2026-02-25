from pydantic import BaseModel

# Model for creating a new user [cite: 60]
class UserCreate(BaseModel):
    name: str
    email: str

# Model representing a user with an ID [cite: 60]
class User(BaseModel):
    id: int
    name: str
    email: str