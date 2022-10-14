from sqlalchemy.orm import Session
from models import User, Flats
import schemas

def get_user(db: Session):
    users = db.query(User).all()
    return users

def create_user(db: Session, user: schemas.UserCreate):
    user = User(username = user.username,
    email = user.email,
    password = user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_flat(db: Session, flats_id: int):
    flats = db.query(Flats).filter(Flats.id == id).all()
    return flats


def get_flats(db: Session):
    all_flats = db.query(Flats).all()
    return all_flats

def  new_flat(db: Session, flat: schemas.newFlat):
    flat = Flats(id = flat.id, bhk = flat.bhk, floors = flat.floors, rent = flat.rent, status=flat.status)
    db.add(flat)
    db.commit()
    db.refresh(flat)
    return flat

