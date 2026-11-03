from fastapi.testclient import TestClient

from main import app, products

client = TestClient(app)


def setup_function():
    products.clear()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_add_and_list_product():
    body = {"name": "Screws box", "quantity": 50, "location": "A1"}
    assert client.post("/products", json=body).status_code == 200
    assert client.get("/products").json() == [body]


def test_get_missing_product_returns_404():
    assert client.get("/products/5").status_code == 404


def test_invalid_quantity_returns_422():
    body = {"name": "Screws box", "quantity": "many", "location": "A1"}
    assert client.post("/products", json=body).status_code == 422


def test_delete_product():
    body = {"name": "Bolts box", "quantity": 30, "location": "A2"}
    client.post("/products", json=body)
    assert client.delete("/products/0").status_code == 200
    assert client.get("/products").json() == []
