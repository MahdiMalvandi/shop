from fastapi import FastAPI
from settings.info import *
from routes import (
    users,
    products,
    orders,
    basket
)

app = FastAPI(title=TITLE, description=DESCRIPTION, contact=CONTACT)

app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(basket.router)
