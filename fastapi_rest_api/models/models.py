from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    login: str
    email: EmailStr
    age: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "login": "User",
                    "email": "user@email.com",
                    "age": 20
                }
            ]
        }
    }


class Product(BaseModel):
    id: int
    product_name: str
    product_cnt: int
    is_available: bool

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "product_name": "Table",
                    "product_cnt": 10,
                    "is_available": True
                }
            ]
        }
    }


class Cart(BaseModel):
    id: int
    user_mail: EmailStr
    product_id: int
    product_count: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "product_count": 20
                }
            ]
        }
    }

