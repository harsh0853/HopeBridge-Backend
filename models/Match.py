from pydantic import BaseModel , EmailStr
from typing import Literal

class Match(BaseModel):
    donation_id: str
    request_id: str
    assigned_by: str
    status: Literal["assigned", "in_progress", "delivered", "cancelled"] = "assigned"
    volunteer_id: Optional[str] = None