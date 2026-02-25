import json
import os
from fastapi import APIRouter, HTTPException
from schema import User, UserCreate

router = APIRouter() 
DB_FILE = "users.txt" 

# Helper functions for data persistence 
def read_users():
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def write_users(users):
    with open(DB_FILE, "w") as file:
        json.dump(users, file, indent=4)

def get_next_id(users):
    if not users:
        return 1
    return max(user['id'] for user in users) + 1

# API Endpoints 

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    users = read_users()
    new_user = {"id": get_next_id(users), "name": user.name, "email": user.email}
    users.append(new_user)
    write_users(users)
    return new_user

@router.get("/", response_model=list[User])
def get_all_users():
    return read_users()

@router.get("/search", response_model=list[User])
def search_users(q: str):
    users = read_users()
    return [u for u in users if q.lower() in u['name'].lower()]

@router.get("/{id}", response_model=User)
def get_user_by_id(id: int):
    users = read_users()
    user = next((u for u in users if u['id'] == id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{id}", response_model=User)
def update_user(id: int, user_update: UserCreate):
    users = read_users()
    for u in users:
        if u['id'] == id:
            u['name'] = user_update.name
            u['email'] = user_update.email
            write_users(users)
            return u
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{id}")
def delete_user(id: int):
    users = read_users()
    updated_users = [u for u in users if u['id'] != id]
    if len(updated_users) == len(users):
        raise HTTPException(status_code=404, detail="User not found")
    write_users(updated_users)

    return {"message": "User deleted successfully"}
