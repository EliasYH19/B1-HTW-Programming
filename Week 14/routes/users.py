from fastapi import APIRouter, HTTPException
from schema import User, UserCreate
from user_store import UserStore # Import the new class

router = APIRouter()
# Initialize the Store 
store = UserStore("users.txt")

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    users = store.load()
    new_id = max([u['id'] for u in users], default=0) + 1
    new_user = {"id": new_id, "name": user.name, "email": user.email}
    users.append(new_user)
    store.save(users)
    return new_user

@router.get("/", response_model=list[User])
def get_all_users():
    return store.load()

@router.get("/{id}", response_model=User)
def get_user_by_id(id: int):
    user = store.find_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{id}")
def update_user(id: int, user_update: UserCreate):
    success = store.update_user(id, user_update.dict())
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}

@router.delete("/{id}")
def delete_user(id: int):
    success = store.delete_user(id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}
