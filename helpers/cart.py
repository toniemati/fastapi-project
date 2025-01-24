from collections import deque

carts = []


def create_cart():
    cart_id = len(carts) + 1

    cart = {
        'cart_id': cart_id,
        'items': deque()
    }

    carts.append(cart)

    return cart


def add_to_cart(cart_id, product_id):
    carts[cart_id - 1]['items'].append(product_id)

    return carts[cart_id - 1]


def pop_from_cart(cart_id):
    return carts[cart_id - 1]['items'].pop()
