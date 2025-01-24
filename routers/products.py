from typing import Annotated

from fastapi import APIRouter, HTTPException, Query  # type: ignore
from sqlmodel import select  # type: ignore

from projekt.db import SessionDep  # type: ignore
from projekt.helpers.binarysearch import binary_search  # type: ignore
from projekt.helpers.quicksort import quicksort  # type: ignore
from projekt.models.product import Product  # type: ignore

router = APIRouter()


@router.get("/products/sorted")
def get_sorted_products_by_price(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
    order: str = "asc"
) -> list[Product]:
    products = session.exec(select(Product).offset(offset).limit(limit)).all()

    sorted_products = quicksort(products, 'price', order)

    return sorted_products


@router.get('/products/find')
def find_products_by_name(
    session: SessionDep,
    name: str
) -> Product:
    products = session.exec(select(Product).order_by(Product.name)).all()

    found_product = binary_search(products, name)

    if not found_product:
        raise HTTPException(status_code=404, detail="Product not found")

    return found_product
