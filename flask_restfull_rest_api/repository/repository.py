from typing import List
from models.models import User, Product, Cart

users_list: List[User] = list()
products_list: List[Product] = list()
carts_list: List[Cart] = list()


class UsersRepository:
    @staticmethod
    def get_users():
        return users_list

    @staticmethod
    def get_user_by_id(user_id):
        for user in users_list:
            if user.id == user_id:
                return user

        return None

    @staticmethod
    def create_user(user):
        users_list.append(user)

    @staticmethod
    def update_user(user_id, login, email, age) -> bool:
        user: User = UsersRepository.get_user_by_id(user_id)
        if user is None:
            return False

        user.login = login
        user.email = email
        user.age = age
        return True

    @staticmethod
    def delete_user(user_id) -> bool:
        if len(users_list) == 0:
            return True

        idx = -1
        for i in range(len(users_list)):
            if users_list[i].id == user_id:
                idx = i
                break

        if idx != -1:
            users_list.pop(idx)
            return True

        return False

    @staticmethod
    def get_next_user_id():
        if len(users_list) == 0:
            return 1
        else:
            return users_list[-1].id + 1


class ProductsRepository:
    @staticmethod
    def get_products():
        return products_list

    @staticmethod
    def get_product(product_id):
        for product in products_list:
            if product.id == product_id:
                return product

        return None

    @staticmethod
    def create_product(product):
        products_list.append(product)

    @staticmethod
    def update_product_count(product_id, count):
        for product in products_list:
            if product.id == product_id:
                product.product_cnt = count

    @staticmethod
    def update_product_availability(product_id, availability):
        for product in products_list:
            if product.id == product_id:
                product.is_available = availability

    @staticmethod
    def update_product(product_id, product_name, product_cnt, is_available) -> bool:
        product: Product = ProductsRepository.get_product(product_id)
        if product is None:
            return False

        product.product_name = product_name
        product.product_cnt = product_cnt
        product.is_available = is_available
        return True

    @staticmethod
    def delete_product(product_id) -> bool:
        if len(products_list) == 0:
            return True

        idx = -1
        for i in range(len(products_list)):
            if products_list[i].id == product_id:
                idx = i
                break

        if idx != -1:
            products_list.pop(idx)
            return True

        return False

    @staticmethod
    def get_next_product_id():
        if len(products_list) == 0:
            return 1

        return products_list[-1].id + 1


class CartRepository:
    @staticmethod
    def get_cart_by_user_id(user_id):
        user: User = UsersRepository.get_user_by_id(user_id)
        user_cart = []

        if user is None:
            return user_cart

        for cart in carts_list:
            if cart.user_mail == user.email:
                user_cart.append(cart)

        return user_cart

    @staticmethod
    def create_cart(cart):
        carts_list.append(cart)

    @staticmethod
    def update_cart(cart: Cart):
        for c in carts_list:
            if c.id == cart.id:
                c.user_mail = cart.user_mail
                c.product_id = cart.product_id
                c.product_count = cart.product_count

    @staticmethod
    def delete_cart(cart_id) -> bool:
        if len(carts_list) == 0:
            return True

        idx = -1
        for i in range(len(carts_list)):
            if carts_list[i].id == cart_id:
                idx = i
                break

        if idx == -1:
            return False

        carts_list.pop(idx)
        return True

    @staticmethod
    def get_next_cart_id():
        if len(carts_list) == 0:
            return 1

        return carts_list[-1].id + 1
