from app import create_app, db
from app.models import User, Product
import random

app = create_app()

with app.app_context():
    # Create tables
    db.create_all()
    
    # Add test user
    if not User.query.filter_by(email='test@example.com').first():
        user = User(email='test@example.com')
        user.set_password('password')
        db.session.add(user)
    
    # Add mock products
    categories = ['electronics', 'books', 'clothing', 'home']
    
    electronics = [
        "Smartphone", "Laptop", "Headphones", "Smart Watch", 
        "Tablet", "Camera", "Speaker", "Gaming Console"
    ]
    books = [
        "Novel", "Textbook", "Biography", "Cookbook", 
        "Mystery", "Science Fiction", "Fantasy", "History"
    ]
    clothing = [
        "T-Shirt", "Jeans", "Jacket", "Dress", 
        "Sweater", "Shorts", "Skirt", "Coat"
    ]
    home = [
        "Lamp", "Chair", "Table", "Sofa", 
        "Bed", "Desk", "Cabinet", "Mirror"
    ]
    
    all_products = electronics + books + clothing + home
    
    for i, name in enumerate(all_products):
        category = 'electronics' if name in electronics else \
                   'books' if name in books else \
                   'clothing' if name in clothing else 'home'
        
        product = Product(
            name=f"{name} {i+1}",
            description=f"High-quality {name} for everyday use",
            price=round(random.uniform(10.99, 299.99), 2),
            category=category,
            stock=random.randint(10, 100)
        )
        db.session.add(product)
    
    db.session.commit()
    print("Database initialized with mock data.")