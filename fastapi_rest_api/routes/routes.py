from fastapi import APIRouter, Path, HTTPException, status
from models.models import User, Product, Cart


user_router = APIRouter()
product_router = APIRouter()
cart_router = APIRouter()

user_list = []
product_list = []
cart_list = []

"""
Маршрутизация пользователей
"""


@user_router.post("/", status_code=201)
async def add_user(user: User):
    user_list.append(user)
    return {"message": "User added successfully"}


@user_router.get("/", status_code=201)
async def retrieve_user() -> dict:
    return {"users": user_list}


@user_router.get("/{user_id}", status_code=201)
async def get_single_user(user_id: int = Path(..., title="The ID of the user to retrieve.")) -> dict:
    for user in user_list:
        if user.id == user_id:
            return {"user": user
                    }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with supplied ID doesn't exist", )


@user_router.put("/{user_id}", status_code=201)
async def update_user(user_data: User, user_id: int = Path(..., title="The ID of the user to be updated")) -> dict:
    for user in user_list:
        if user.id == user_id:
            user.login = user_data.login
            user.email = user_data.email
            user.age = user_data.age
            return {
                "message": "User updated successfully."
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with supplied ID doesn't exist", )


@user_router.delete("/{user_id}", status_code=201)
async def delete_single_user(user_id: int) -> dict:
    for index in range(len(user_list)):
        user = user_list[index]
        if user.id == user_id:
            user_list.pop(index)
            return {
                "message": "User deleted successfully."
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with supplied ID doesn't exist", )


"""
Маршрутизация товаров
"""


@product_router.post("/", status_code=201)
async def add_product(product: Product):
    product_list.append(product)
    return {"message": "Product added successfully"}


@product_router.get("/", status_code=201)
async def retrieve_product() -> dict:
    return {"products": product_list}


@product_router.get("/{product_id}", status_code=201)
async def get_single_product(product_id: int = Path(..., title="The ID of the user to retrieve.")) -> dict:
    for product in product_list:
        if product.id == product_id:
            return {"product": product
                    }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product with supplied ID doesn't exist", )


@product_router.put("/{product_id}", status_code=201)
async def update_product(product_data: Product, product_id: int = Path(...,
                                                                       title="The ID of the user to be updated"))\
        -> dict:
    for product in product_list:
        if product.id == product_id:
            product.product_name = product_data.product_name
            product.product_cnt = product_data.product_cnt
            product.is_available = product_data.is_available
            return {
                "message": "Product updated successfully."
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product with supplied ID doesn't exist", )


@product_router.delete("/{product_id}", status_code=201)
async def delete_single_product(product_id: int) -> dict:
    for index in range(len(product_list)):
        product = product_list[index]
        if product.id == product_id:
            product_list.pop(index)
            return {
                "message": "Product deleted successfully."
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product with supplied ID doesn't exist", )

"""
Маршрутизация корзины товаров
"""


@cart_router.get("/{cart_id}", status_code=201)
async def get_single_cart(cart_id: int = Path(..., title="The ID of the cart to retrieve.")) -> dict:
    for cart in cart_list:
        if cart.id == cart_id:
            return {"cart": cart
                    }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product with supplied ID doesn't exist", )


@cart_router.put("/{user_id}", status_code=201)
async def update_cart(product_data: Product, user_id: int = Path(..., title="The ID of the cart to be updated"))\
        -> dict:
    user = None
    for u in user_list:
        if u.id == user_id:
            user = u
            break

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart with supplied ID doesn't exist", )

    user_email = user.email
    cart = None
    for c in cart_list:
        if c.user_mail == user_email:
            cart = c
            break

    if cart is None:
        cart = Cart()
        cart.user_mail = user_email
        cart.product_id = product_data.id
        cart.product_count = 0
        if len(cart_list) == 0:
            cart.id = 1
        else:
            cart.id = cart_list[-1].id + 1

    is_added = False

    for product in product_list:
        if product.is_available:
            if product.id == product_data.id:
                current_count = product.product_cnt - product_data.product_cnt
                if current_count < 0:
                    break
                else:
                    product.product_cnt = current_count
                    cart.product_count = product_data.product_cnt
                    is_added = True
                    break

    if is_added:
        cart_list.append(cart)
        return {
            "message": "Cart updated successfully."
        }

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart with supplied ID doesn't exist", )


@cart_router.delete("/{cart_id}", status_code=201)
async def delete_single_cart(cart_id: int) -> dict:
    for index in range(len(product_list)):
        cart = cart_list[index]
        if cart.id == cart_id:
            cart_list.pop(index)
            return {
                "message": "Сart deleted successfully."
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Сart with supplied ID doesn't exist", )