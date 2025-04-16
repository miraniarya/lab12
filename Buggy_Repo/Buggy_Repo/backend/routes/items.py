from fastapi import APIRouter, HTTPException
from models import Item
from bson import ObjectId

router = APIRouter()  # Fixed: Changed from dictionary to APIRouter()

async def get_items_collection():
    from db import init_db
    return init_db()["items_collection"]

@router.get("/")
async def get_items():
    collection = await get_items_collection()
    items = []
    async for item in collection.find():
        item["_id"] = str(item["_id"])
        items.append(item)
    return items

@router.post("/")
async def create_item(item: Item):
    collection = await get_items_collection()
    result = await collection.insert_one(item.dict())
    return {"id": str(result.inserted_id)}

# Removed duplicate @router.post("/") decorator

@router.delete("/{item_id}")
async def delete_item(item_id: str):
    collection = await get_items_collection()
    try:
        object_id = ObjectId(item_id)  # Validate ObjectId
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid item_id format")
    
    result = await collection.delete_one({"_id": object_id})
    if result.deleted_count:
        return {"status": "deleted", "deleted_item_id": item_id}
    raise HTTPException(status_code=404, detail="Item not found")
