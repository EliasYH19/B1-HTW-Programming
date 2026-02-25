from fastapi import APIRouter, HTTPException
from schema import User, UserCreate
from user_store import UserStore

router = APIRouter()
# Initialize the Store with a .db file [cite: 174]
store = UserStore("users.db")

@router.get("/", response_model=list[User])
def get_users():
    """Uses store.load() to fetch all users from SQLite[cite: 176, 177]."""
    return store.load()

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    """Saves the new user directly to the database[cite: 187, 188]."""
    store.save(user.dict())
    # Note: SQLite handles ID autoincrement automatically [cite: 164]
    return {"id": 0, **user.dict()} # ID 0 is a placeholder; real ID is in DB

@router.put("/{user_id}")
def update_user_endpoint(user_id: int, user_update: UserCreate):
    """Calls store.update_user() with SQL logic[cite: 199]."""
    if not store.update_user(user_id, user_update.dict()):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}

@router.delete("/{user_id}")
def delete_user_endpoint(user_id: int):
    """Calls store.delete_user() with SQL logic[cite: 201]."""
    if not store.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}