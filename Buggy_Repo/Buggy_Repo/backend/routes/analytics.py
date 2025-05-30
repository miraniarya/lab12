from fastapi import APIRouter
from fastapi.responses import JSONResponse
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

router = APIRouter()

# Efficient DB init
from db import init_db

async def get_items_collection():
    return init_db()["items_collection"]

async def get_users_collection():
    return init_db()["users_collection"]

@router.get("/analytics")
async def get_analytics():
    try:
        items_collection = await get_items_collection()
        users_collection = await get_users_collection()

        items = []
        async for item in items_collection.find():
            items.append(item)

        users = []
        async for user in users_collection.find():
            users.append(user)
    except Exception as e:
        return JSONResponse({"error": f"Database error: {str(e)}"}, status_code=500)

    item_name_lengths = np.array([len(item.get("names", "")) for item in items]) if items else np.array([])
    user_username_lengths = np.array([len(user.get("usernames", "")) for user in users]) if users else np.array([])

    item_count = len(items)
    user_count = len(users)

    stats = {
        "item_count": item_count,
        "user_count": user_count,
        "avg_item_name_length": float(item_name_lengths.mean()) if item_name_lengths.size > 0 else 0.0,
        "avg_user_username_length": float(user_username_lengths.mean()) if user_username_lengths.size > 0 else 0.0,
        "max_item_name_length": int(item_name_lengths.max()) if item_name_lengths.size > 0 else 0,
        "max_user_username_length": int(user_username_lengths.max()) if user_username_lengths.size > 0 else 0,
    }

    # If no data, return error to help frontend display message
    if item_name_lengths.size == 0 and user_username_lengths.size == 0:
        return JSONResponse({"error": "No data available to plot.", "stats": stats}, status_code=200)

    # Create histogram
    plt.figure(figsize=(8, 6))
    if item_name_lengths.size > 0:
        plt.hist(item_name_lengths, bins=10, alpha=0.5, label="Item Names", color="blue")
    if user_username_lengths.size > 0:
        plt.hist(user_username_lengths, bins=10, alpha=0.5, label="Usernames", color="green")
    plt.title("Distribution of Name Lengths")
    plt.xlabel("Length")
    plt.ylabel("Frequency")
    plt.legend()

    # Save plot to base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    plt.close()

    return JSONResponse({
        "stats": stats,
        "plot": f"data:image/png;base64,{image_base64}"
    })
