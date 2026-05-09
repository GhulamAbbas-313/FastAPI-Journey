from fastapi import FastAPI
from models import Inventory

app=FastAPI()

inventory = [
    Inventory(id= 1, name= "Laptop", stock= 5),
    Inventory(id= 2, name= "Mouse", stock= 10)
]

@app.put("/update-stock/{p_id}")
async def update_stock(p_id: int, add_quantity: int):
    for items in inventory:
        if items.id == p_id:
            items.stock += add_quantity
            return items
    else:
        return {'message':'Product not found'}
            
