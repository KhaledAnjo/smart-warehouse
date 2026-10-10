from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
	return{"message": "Smart Warehouse API is running"}
