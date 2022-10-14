from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session
import crud, models, schemas
from database import Base,engine,  get_db

Base.metadata.create_all(engine)

app = FastAPI()


@app.post("/flats",response_model=schemas.showFlat)
def new_flat(flat:schemas.newFlat, db: Session = Depends(get_db)):
    newflat = models.Flats(bhk = flat.bhk,floors=flat.floors ,rent = flat.rent, sqft_area = flat.sqft_area)
    db.add(newflat)
    db.commit()
    db.refresh(newflat)
    return newflat


@app.get("/", response_model = List[schemas.showFlat])
def read_flats(db: Session = Depends(get_db)):
        flats = crud.get_flats(db)
        return flats



