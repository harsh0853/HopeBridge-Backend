# routes/request.py
from fastapi import APIRouter, Depends, HTTPException
from db.db import db
from models.Request import Request
from datetime import datetime
from middleware.auth import get_current_user, require_role

router = APIRouter()

@router.post("/")
async def create_request(
    request: Request,
    user=Depends(require_role("ngo"))
):
    request_dict = request.dict()
    request_dict["ngo_id"] = user["user_id"]
    request_dict["created_at"] = datetime.utcnow()
    request_dict["updated_at"] = datetime.utcnow()

    await db.requests.insert_one(request_dict)
    return {"message": "Request created successfully"}

@router.get("/")
async def list_requests(user=Depends(get_current_user)):
    cursor = db.requests.find({"ngo_id": user["user_id"]})
    requests = []
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        requests.append(doc)
    return requests
