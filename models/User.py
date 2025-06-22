from pydantic import BaseModel , EmailStr
from typing import Literal

class User(BaseModel):
    name : str
    email : EmailStr
    password : str
    role : Literal["ngo" , "donor" , "volunteer"]