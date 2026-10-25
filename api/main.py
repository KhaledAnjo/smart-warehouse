from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# temporary storage in memory (i will replace it with PostgreSQL later)
products = []


class Product(BaseModel):
    name: str
    quantity: int
    location: str


@app.get("/")
def read_root():
    return {"message": "Smart Warehouse API is running"}


@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return product


@app.get("/products")
def list_products():
    return products
