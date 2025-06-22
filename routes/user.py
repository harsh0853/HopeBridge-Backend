from fastapi import APIRouter , HTTPException
from jose import jwt
from models.User import User
import os 
from passlib.hash import bcrypt
from db.db import db

router = APIRouter()
jwt_secret = "supersecretsothatyoucanseehere"
@router.post("/register")
async def register(user : User):
    if await db.users.find_one({"email":user.email}):
        raise HTTPException(status_code=400 , detail="User already exist")
    userd = user.dict()
    userd["password"] = bcrypt.hash(user.password)

    await db.users.insert_one(userd)
    return  {"message" : "User registered successfully"}

@router.post("/login")
async def login(user : User):
    db_user = db.users.find_one({"email":user.email})
    if not db_user or not bcrypt.verify(user.password , db_user["password"]):
        raise HTTPException(status_code=401 , detail="Incorrect credentials")
    payload = {
        "user_id" : str(db_user["_id"]),
        "role" : db_user["role"]
    }

    toekn = jwt.encode(payload , jwt_secret , algorithm="HS256")
    return {"token":toekn , "token_type":"bearer" }

     