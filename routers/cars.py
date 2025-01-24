from typing import Annotated

from fastapi import APIRouter, HTTPException, Query  # type: ignore
from sqlmodel import select  # type: ignore

from projekt.db import SessionDep  # type: ignore
from projekt.models.car import Car  # type: ignore

router = APIRouter()


@router.get("/cars")
def read_cars(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Car]:
    cars = session.exec(select(Car).offset(offset).limit(limit)).all()

    return cars


@router.get("/cars/{car_id}")
def read_car(
    car_id: int,
    session: SessionDep
) -> Car:
    car = session.get(Car, car_id)

    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car


@router.post("/cars")
def create_car(
    car: Car,
    session: SessionDep
) -> Car:
    session.add(car)
    session.commit()
    session.refresh(car)

    return car


@router.put("/cars/{car_id}", response_model=Car)
def update_car(
    car_id: int,
    car: Car,
    session: SessionDep
) -> Car:
    car_db = session.get(Car, car_id)

    if not car_db:
        raise HTTPException(status_code=404, detail="Car not found")

    car_data = car.model_dump(exclude_unset=True)
    car_db.sqlmodel_update(car_data)

    session.add(car_db)
    session.commit()
    session.refresh(car_db)

    return car_db


@router.delete("/cars/{car_id}")
def delete_car(
    car_id: int,
    session: SessionDep
) -> dict[str, bool]:
    car = session.get(Car, car_id)

    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    session.delete(car)
    session.commit()

    return {"ok": True}
