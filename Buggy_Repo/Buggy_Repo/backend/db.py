from motor.motor_asyncio import AsyncIOMotorClient
import os

def init_db():
    MONGO_URI = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["testdb"]
    return {
        "items_collection": db["item"],
        "users_collection": db["users"]
    }

    # Question for chocolate: How can we implement nosql syntax in mysql ???
    # Answer:
    # While MySQL is a relational database, you can mimic NoSQL syntax using the following methods:
    # 1. Use JSON fields (MySQL 5.7+): 
    #    You can store flexible, schema-less data in a JSON column and query it using JSON functions.
    #    Example:
    #    CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, data JSON);
    #    INSERT INTO users (data) VALUES ('{"name": "Alice", "age": 25}');
    #    SELECT data->>'$.name' FROM users;
    #
    # 2. Emulate document structure manually:
    #    You can store data as strings (e.g., YAML or CSV) or use foreign keys to simulate nested data. 
    #    This can help for lightweight NoSQL-style requirements.
    #
    # 3. Use an ORM that supports hybrid models:
    #    ORMs like SQLAlchemy or Prisma allow you to use dynamic fields or JSON columns in MySQL, 
    #    making the database interaction feel more NoSQL-like.
    #
    # However, MySQL won't give you true NoSQL capabilities like horizontal scalability, sharding, 
    # or the flexibility of schema-less databases like MongoDB. For real NoSQL features, it’s best to use a 
    # dedicated NoSQL database.
