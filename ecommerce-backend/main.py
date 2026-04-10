from fastapi import FastAPI
from database import users_collection,products_collection,cart_collection,orders_collection
from models import User, Product, CartItem, Order ,UserAuth

app = FastAPI()


#Home
@app.get("/")
def home():
    return {"message":"E- commerce API running"}


#Create User
@app.post("/user")
def create_user(user: User):
    users_collection.insert_one(user.model_dump())
    return {"message": "User created"}


#Add Product
@app.post("/product")
def add_product(product:Product):
    products_collection.insert_one(product.model_dump())
    return {"message": "Product added"}


#Get Products
@app.get("/products")
def get_products():
    products = list(products_collection.find({}, {"_id": 0}))
    return {"products": products}


#Add to Cart
@app.post("/cart")
def add_to_cart(item: CartItem):
    cart_collection.insert_one(item.model_dump())
    return {"message": "Item added to cart"}
    
    
#View Cart
@app.get("/cart/{user_email}")
def view_cart(user_email: str):
    items = list(cart_collection.find({"user_email":user_email}, {"_id": 0}))
    return {"cart": items}


#Remove from cart 
@app.delete("/cart")
def remove_from_cart(item: CartItem):
    cart_collection.delete_one({
        "user_email": item.user_email,
        "product_name": item.product_name })
    return {"message": "Item removed"}


#ORDER API
@app.post("/order/{user_email}")
def place_order(user_email: str):
    cart_items = list(cart_collection.find({"user_email": user_email}, {"_id": 0}))
    
    print("DEBUG CART:", cart_items)
    if not cart_items:
        return {"error": "Cart is empty"}
    
    total = 0
    
    for item in cart_items:
        product = products_collection.find_one({"name": item["product_name"]})
        
        print("DEBUG PRODUCT:", product)
        if not product:
            return {"error": f"Poduct not found: {item['product_name']}"}
            
        total += product["price"]*item["quantity"]
            
    Order = {
        "user_email":user_email,
        "products": cart_items,
        "total_amount": total 
    }
    
    orders_collection.insert_one(Order)
    
    #Clear cart after order
    cart_collection.delete_many({"user_email": user_email})
    
    return {"message": "Order placed", "total":total}


@app.get("/order/{user_email}")
def get_orders(user_email: str):
    orders = list(orders_collection.find({"user_email": user_email}, {"_id": 0}))
    return {"orders": orders}


@app.post("/login")
def login(user: UserAuth):
    existing = users_collection.find_one({"email": user.email})

    if not existing:
        return {"error": "User not found"}

    if existing["password"] != user.password:
        return {"error": "Invalid password"}

    return {"message": "Login successful"}


@app.post("/signup")
def signup(user: UserAuth):
    existing = users_collection.find_one({"email": user.email})
    
    if existing:
        return {"error": "User already exists"}
    
    users_collection.insert_one(user.model_dump())
    
    return {"message": "User registered"}