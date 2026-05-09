from fastapi import FastAPI
from models import Product

app = FastAPI()
@app.post("/add-product")
async def inputt(item: Product): 
    return {
        "message": "Product validated!",
        "data": item
    }
