from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Smart Warehouse API")

# temporary in-memory storage (PostgreSQL is planned)
products = []


class Product(BaseModel):
    name: str
    quantity: int
    location: str


@app.get("/")
def read_root():
    return {"message": "Smart Warehouse API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return product


@app.get("/products")
def list_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id < 0 or product_id >= len(products):
        raise HTTPException(status_code=404, detail="Product not found")
    return products[product_id]


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id < 0 or product_id >= len(products):
        raise HTTPException(status_code=404, detail="Product not found")
    return products.pop(product_id)


@app.delete("/products")
def clear_products():
    products.clear()
    return {"message": "All products deleted"}
