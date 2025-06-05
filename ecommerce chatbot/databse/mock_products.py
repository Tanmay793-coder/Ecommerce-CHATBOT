import random
from faker import Faker
from app import create_app
from app.models import db, Product

fake = Faker()

def generate_mock_products(count=100):
    """Generate realistic mock product data"""
    categories = {
        'electronics': [
            'Smartphone', 'Laptop', 'Headphones', 'Smart Watch',
            'Tablet', 'Camera', 'Bluetooth Speaker', 'Gaming Console',
            'Fitness Tracker', 'Wireless Earbuds', 'External Hard Drive',
            'Monitor', 'Keyboard', 'Mouse', 'Router'
        ],
        'books': [
            'Science Fiction Novel', 'Mystery Thriller', 'Romance Book',
            'Biography', 'History Book', 'Cookbook', 'Self-Help Guide',
            'Fantasy Novel', 'Business Book', 'Art Book',
            'Travel Guide', 'Poetry Collection', 'Science Textbook',
            'Children\'s Book', 'Graphic Novel'
        ],
        'clothing': [
            'T-Shirt', 'Jeans', 'Jacket', 'Dress',
            'Sweater', 'Shorts', 'Skirt', 'Coat',
            'Hoodie', 'Suit', 'Blouse', 'Polo Shirt',
            'Leggings', 'Swimsuit', 'Winter Hat'
        ],
        'home': [
            'Desk Lamp', 'Dining Chair', 'Coffee Table', 'Sofa',
            'Bed Frame', 'Bookshelf', 'Cabinet', 'Mirror',
            'Rug', 'Curtains', 'Throw Pillow', 'Blanket',
            'Wall Art', 'Vase', 'Cutlery Set'
        ]
    }

    products = []
    for _ in range(count):
        category = random.choice(list(categories.keys()))
        name = random.choice(categories[category])
        brand = fake.company() if category == 'electronics' else None
        product_name = f"{brand + ' ' if brand else ''}{name} {fake.random_int(1, 1000)}"
        
        products.append({
            'name': product_name,
            'description': generate_description(category, name),
            'price': generate_price(category),
            'category': category,
            'stock': random.randint(5, 100)
        })
    
    return products

def generate_description(category, product_name):
    """Generate realistic product descriptions"""
    descriptors = {
        'electronics': [
            f"High-performance {product_name} with advanced features",
            f"Latest model {product_name} with premium components",
            f"Professional-grade {product_name} for demanding users"
        ],
        'books': [
            f"Bestselling {product_name} by award-winning author",
            f"New edition of the classic {product_name}",
            f"Critically acclaimed {product_name} with rave reviews"
        ],
        'clothing': [
            f"Comfortable and stylish {product_name} for everyday wear",
            f"Premium quality {product_name} made with sustainable materials",
            f"Trendy {product_name} perfect for any occasion"
        ],
        'home': [
            f"Beautiful {product_name} that enhances your living space",
            f"Durable {product_name} built to last for years",
            f"Modern design {product_name} for contemporary homes"
        ]
    }
    return random.choice(descriptors[category])

def generate_price(category):
    """Generate category-appropriate prices"""
    price_ranges = {
        'electronics': (99.99, 1999.99),
        'books': (4.99, 39.99),
        'clothing': (14.99, 299.99),
        'home': (19.99, 999.99)
    }
    min_price, max_price = price_ranges[category]
    return round(random.uniform(min_price, max_price), 2)

def seed_database():
    """Seed the database with mock products"""
    app = create_app()
    with app.app_context():
        # Clear existing products
        Product.query.delete()
        
        # Generate and add new products
        products = generate_mock_products(100)
        for product_data in products:
            product = Product(**product_data)
            db.session.add(product)
        
        db.session.commit()
        print(f"Successfully added {len(products)} mock products to the database")

if __name__ == '__main__':
    seed_database()