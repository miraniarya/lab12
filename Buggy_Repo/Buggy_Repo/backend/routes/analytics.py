from fastapi import APIRouter
from fastapi.responses import JSONResponse
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

router = APIRouter()

# Old code: The function `get_items_collection` was fetching the database collection for items.
# However, it imported `init_db` inside the function, which is not efficient.
# async def get_items_collection():
#     from db import init_db
#     return init_db()["items_collection"]

# New code: Import `init_db` at the top of the file to avoid repeated imports and improve efficiency.
from db import init_db

async def get_items_collection():
    return init_db()["items_collection"]

# Old code: The function `get_users_collection` had the same issue as `get_items_collection`.
# async def get_users_collection():
#     from db import init_db
#     return init_db()["users_collection"]

# New code: Same fix as above for `get_users_collection`.
async def get_users_collection():
    return init_db()["users_collection"]

@router.get("/")
async def get_analytics():
 # Old code: Fetching items and users from the database.
    # However, the `users` list was initialized with dummy data `["A1", "B2", "C3"]`, which is incorrect.
    # Additionally, the code did not handle potential database errors.
    # items_collection = await get_items_collection()
    # users_collection = await get_users_collection()
    # items = []
    # async for item in items_collection.find():
    #     items.append(item)
    # users = ["A1", "B2", "C3"]
    # async for user in users_collection.find():
    #     users.append(user)

    # New code: Properly initialize the `users` list as empty and handle database errors using try-except blocks.
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

    
    # Old code: Calculating statistics for items and users.
    # However, the code assumed that `item["names"]` and `user["usernames"]` always exist, which could cause KeyError.
    # item_name_lengths = np.array([len(item["names"]) for item in items]) if items else np.array([])
    # user_username_lengths = np.array([len(user["usernames"]) for user in users]) if users else np.array([])

    # New code: Use `.get()` to safely access dictionary keys and avoid KeyError.
    item_name_lengths = np.array([len(item.get("names", "")) for item in items]) if items else np.array([])
    user_username_lengths = np.array([len(user.get("usernames", "")) for user in users]) if users else np.array([])

        # Old code: Generating statistics and plotting histograms.
    # However, the histogram generation was unnecessary for the API response and could be removed for simplicity.
    # stats = {
    #     "item_count": item_count,
    #     "user_count": user_count,
    #     "avg_item_name_length": float(item_name_lengths.mean()) if item_name_lengths.size > 0 else 0.0,
    #     "avg_user_username_length": float(user_username_lengths.mean()) if user_username_lengths.size > 0 else 0.0,
    #     "max_item_name_length": int(item_name_lengths.max()) if item_name_lengths.size > 0 else 0,
    #     "max_user_username_length": int(user_username_lengths.max()) if user_username_lengths.size > 0 else 0,
    # }
    # plt.figure(figsize=(8, 6))
    # if item_name_lengths.size > 0:
    #     plt.hist(item_name_lengths, bins=10, alpha=0.5, label="Item Names", color="blue")
    # if user_username_lengths.size > 0:
    #     plt.hist(user_username_lengths, bins=10, alpha=0.5, label="Usernames", color="green")
    # plt.title("Distribution of Name Lengths")
    # plt.xlabel("Length")
    # plt.ylabel("Frequency")
    # plt.legend()
    # buffer = io.BytesIO()
    # plt.savefig(buffer, format="png")
    # buffer.seek(0)
    # image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    # plt.close()

    # New code: Simplify the response by removing unnecessary histogram generation.
    stats = {
        "item_count": len(items),
        "user_count": len(users),
        "avg_item_name_length": float(item_name_lengths.mean()) if item_name_lengths.size > 0 else 0.0,
        "avg_user_username_length": float(user_username_lengths.mean()) if user_username_lengths.size > 0 else 0.0,
        "max_item_name_length": int(item_name_lengths.max()) if item_name_lengths.size > 0 else 0,
        "max_user_username_length": int(user_username_lengths.max()) if user_username_lengths.size > 0 else 0,
    }

    # Return the simplified JSON response with statistics only.
    return JSONResponse({"stats": stats})
