from pydantic import BaseModel , EmailStr
from typing import Literal

class Request(BaseModel):
    item_needed: str
    ngo_id : str
    category: str 
    quantity: int
    urgency: int 
    status: Literal["pending", "approved", "fulfilled"] = "pending"
    reason: Optional[str] = None
    location: Optional[str] = None