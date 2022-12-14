from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session as DbSession

from app.dependencies.database import get_db
from app.database.models.city import City
from app.schema.city import CityInput, CityOutput

city_router = APIRouter()


@city_router.get("/", tags=['Cities'], response_model=List[CityOutput])
def _list(skip: int = 0, limit: int = 10, db: DbSession = Depends(get_db)):
    return City.get_list(db=db, skip=skip, limit=limit)


@city_router.get('/{city_id}', tags=['Cities'], response_model=CityOutput)
def retrieve(city_id: int, db: DbSession = Depends(get_db)):
    return City.get_by_id(db=db, _id=city_id)


@city_router.post('/', tags=['Cities'], response_model=CityOutput)
def create(city: CityInput, db: DbSession = Depends(get_db)):
    return City.create(data=city, db=db)


@city_router.put('/{city_id}', tags=['Cities'], response_model=CityOutput)
def update(city_id: int, city: CityInput, db: DbSession = Depends(get_db)):
    return City.update(data=city, _id=city_id, db=db)
