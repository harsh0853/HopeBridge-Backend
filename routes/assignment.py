# routes/assignment.py
from fastapi import APIRouter, Depends, HTTPException
from db.mongo import db
from models.assignment import Assignment
from datetime import datetime
from auth import get_current_user, require_role

router = APIRouter()

@router.post("/assign")
async def assign_donation(
    assignment: Assignment,
    user=Depends(require_role("admin"))
):
    match_dict = assignment.dict()
    match_dict["created_at"] = datetime.utcnow()
    match_dict["updated_at"] = datetime.utcnow()

    donation = await db.donations.find_one({"_id": match_dict["donation_id"]})
    request = await db.requests.find_one({"_id": match_dict["request_id"]})
    
    if not donation or not request:
        raise HTTPException(404, "Donation or Request not found")

    await db.assignments.insert_one(match_dict)
    return {"message": "Donation assigned successfully"}

@router.get("/")
async def list_assignments(user=Depends(require_role("admin"))):
    cursor = db.assignments.find()
    assignments = []
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        assignments.append(doc)
    return assignments
