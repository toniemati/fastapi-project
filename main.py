from typing import Annotated

from fastapi import FastAPI  # type: ignore

from projekt.routers.cars import router as cars_router  # type: ignore
from projekt.routers.products import router as products_router  # type: ignore

app = FastAPI()

app.include_router(cars_router)
app.include_router(products_router)


@app.get("/")
async def root():
    return {'hello': 'world'}
