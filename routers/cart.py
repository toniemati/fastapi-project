from fastapi import APIRouter, HTTPException  # type: ignore

from projekt.helpers.cart import (add_to_cart, carts,  # type: ignore
                                  create_cart, pop_from_cart)

router = APIRouter()


@router.post('/cart/create')
def cart_create() -> dict:
    return create_cart()


@router.get('/carts')
def read_carts() -> list[dict]:
    return carts


@router.get('/carts/{cart_id}')
def read_carts(cart_id: int) -> dict:
    try:
        return carts[cart_id - 1]
    except:
        raise HTTPException(status_code=404, detail="Cart not found")


@router.post("/cart/{cart_id}/add/{product_id}")
def add_product_to_cart(
    cart_id: int,
    product_id: int,
) -> dict:
    try:
        return add_to_cart(cart_id, product_id)
    except:
        raise HTTPException(status_code=404, detail="Cart not found")


@router.post("/cart/{cart_id}/pop")
def pop_product_to_cart(cart_id: int) -> int:
    try:
        return pop_from_cart(cart_id)
    except:
        raise HTTPException(status_code=404, detail="Cart not found or empty")
