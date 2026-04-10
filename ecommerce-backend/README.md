# 🛒 Mini Amazon Backend (E-commerce API)

## 📌 Overview
A backend system built using FastAPI and MongoDB that simulates core functionalities of an e-commerce platform like Amazon. It supports user management, product handling, cart operations, order processing, and basic authentication.

---

## 🚀 Features

- User signup & login
- Add & manage products
- Add to cart / remove from cart
- Place orders (cart → order conversion)
- Order history tracking
- MongoDB integration
- REST API design

---

## 🛠 Tech Stack

- FastAPI
- MongoDB
- Python
- Pydantic

---

## 📦 API Endpoints

### Users
- `POST /signup`
- `POST /login`

### Products
- `POST /product`
- `GET /products`

### Cart
- `POST /cart`
- `GET /cart/{user_email}`
- `DELETE /cart`

### Orders
- `POST /order/{user_email}`
- `GET /orders/{user_email}`

---

## 🧠 How it works

1. Users register and login
2. Products are added to database
3. Users add items to cart
4. Orders are placed from cart
5. Cart is cleared automatically
6. Order history is stored and retrievable

---

## ⚙️ Setup

```bash
git clone https://github.com/your-username/ecommerce-backend.git
cd ecommerce-backend
pip install -r requirements.txt
uvicorn main:app --reload