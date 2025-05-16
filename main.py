from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="Simple FastAPI",
    description="A simple FastAPI application",
    version="0.1.0"
)

# Sample data store
items = []

# Item model
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float

# Create routes
@app.get("/")
async def root():
    return {"message": "Welcome to Simple FastAPI"}

@app.get("/items", response_model=List[Item])
async def get_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items", response_model=Item, status_code=201)
async def create_item(item: Item):
    item_dict = item.dict()
    item_dict["id"] = len(items)
    items.append(item_dict)
    return item_dict

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    
    item_dict = item.dict(exclude_unset=True)
    item_dict["id"] = item_id
    items[item_id] = item_dict
    return item_dict

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    
    items.pop(item_id)
    return {"message": "Item deleted successfully"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)