# routes/donation.py
from fastapi import APIRouter, Depends, HTTPException
from db.mongo import db
from models.donation import Donation
from datetime import datetime
from auth import get_current_user, require_role

router = APIRouter()

@router.post("/")
async def create_donation(
    donation: Donation,
    user=Depends(require_role("donor"))
):
    donation_dict = donation.dict()
    donation_dict["donor_id"] = user["user_id"]
    donation_dict["created_at"] = datetime.utcnow()
    donation_dict["updated_at"] = datetime.utcnow()

    await db.donations.insert_one(donation_dict)
    return {"message": "Donation created successfully"}

@router.get("/")
async def list_donations(user=Depends(get_current_user)):
    cursor = db.donations.find({"donor_id": user["user_id"]})
    donations = []
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        donations.append(doc)
    return donations
