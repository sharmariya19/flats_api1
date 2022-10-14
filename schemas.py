from re import I
from typing import List,Union

from pydantic import BaseModel, EmailStr

class user(BaseModel):
    username:str
    email:EmailStr

class UserCreate(user):
    password:str

class ShowUser(user):
    class Config():  
        orm_mode = True

class flat(BaseModel):
    id:int
    bhk : int
    floors: int
    sqft_area: int
    rent:int

class newFlat(flat):
    pass

class showFlat(flat):
    status:str
    class Config:
        orm_mode = True



# class assignFlat():
#     tenant_id:int
#     tenant_name:str
#     flat_id:int

