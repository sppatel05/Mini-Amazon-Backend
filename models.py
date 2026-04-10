from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    
class Product(BaseModel):
    name: str
    price: float
    description: str
    stock: int
    
class CartItem(BaseModel):
    user_email: str
    product_name: str
    quantity: int 
    
class Order(BaseModel):
    user_email: str
    products: list
    total_amount: float
    
class UserAuth(BaseModel):
    email:str
    password:str
