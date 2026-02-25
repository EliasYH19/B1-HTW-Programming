from fastapi import APIRouter, HTTPException
from schema import User, UserCreate
from user_store import UserStore

router = APIRouter()
# Initialize the Store with a .db file
store = UserStore("users.db")

@router.get("/", response_model=list[User])
def get_users():
    return store.load()

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    store.save(user.dict())
    return {"id": 0, **user.dict()} # ID 0 is a placeholder

@router.put("/{user_id}")
def update_user_endpoint(user_id: int, user_update: UserCreate):
    if not store.update_user(user_id, user_update.dict()):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}

@router.delete("/{user_id}")
def delete_user_endpoint(user_id: int):
    if not store.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}
