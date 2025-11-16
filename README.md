# ALX Travel App

## Overview
ALX Travel App is a Django-based web application designed to manage travel listings and related data through a RESTful API.  
This project is part of the ALX backend development curriculum and demonstrates the setup of a Django REST API with proper configuration, Swagger documentation, and database integration.

---

## 🎯 Objective
Set up a Django project with:

- Necessary dependencies
- Database connection (SQLite initially, later MySQL)
- Swagger UI integration for automatic API documentation

---

## 🏗️ Project Structure

---

## Features
- Property listings management  
- Booking system  
- User reviews and ratings  
- RESTful API  

---

## Models

### Listing
- Property details (title, description, address, amenities)  
- Pricing and capacity information  
- Host relationship  

### Booking
- Reservation details (dates, guests, pricing)  
- Status management  
- Guest and listing relationships  

---

## ⚙️ Technologies Used

| Tool                        | Purpose                                  |
|------------------------------|-----------------------------------------|
| Python 3.12+                 | Programming language                     |
| Django                       | Backend web framework                     |
| Django REST Framework (DRF)  | API development                           |
| drf-yasg                     | Swagger/OpenAPI documentation             |
| django-environ               | Environment variable management          |
| django-cors-headers          | Enable cross-origin requests             |
| Celery                        | Task queue for background processing    |
| RabbitMQ                      | Message broker for Celery               |
| MySQL / SQLite               | Database management                      |

---

## 🧩 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/alx_travel_app.git
cd alx_travel_app
