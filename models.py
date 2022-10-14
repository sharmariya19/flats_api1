from ast import For
from enum import unique
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True, index= True)
    name = Column(String)
    email = Column(String, unique=True,index = True)
    hashed_password = Column(String)

class Flats(Base):
    __tablename__ = "flats"

    id = Column(Integer, primary_key = True, index= True)
    bhk = Column(Integer)
    floors = Column(Integer)
    rent = Column(Integer)
    sqft_area = Column(Float)
    status = Column(String , default = "available")


# class FlatAssignment(Base):
#     __tablename__ = "flatassignment"

#     tenant_id = Column(Integer, primary_key = True, index= True)
#     tenant_name = Column(String)
#     flat_id = Column(Integer,ForeignKey("flats.id"))
#     flat = relationship("Flats")

