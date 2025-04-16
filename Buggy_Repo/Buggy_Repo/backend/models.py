#Kimaya checked this file 2 Edits
from pydantic import BaseModel

class Item(BaseModel):#Edit 1: Item class inherits from BaseModel
    name: str #Edit 2: Name type should be str
    description: str

class User(BaseModel):
    username: str
    bio: str
    
    # You can raise your hands and give the answer to the chocolate question
