from pydantic import BaseModel , EmailStr
from typing import Literal

class Donation(BaseModel):
    id : str
    donor_id : str
    category : str
    status : Literal["pending" , "delivered" , "matched"]
    quantity : int
    description : Optional[str] =""