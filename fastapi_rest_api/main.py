from fastapi import FastAPI
import uvicorn
from routes.routes import user_router, product_router, cart_router


app = FastAPI()

app.include_router(user_router, prefix="/user")

app.include_router(product_router, prefix="/product")

app.include_router(cart_router, prefix="/cart")


if __name__ == " main ":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
