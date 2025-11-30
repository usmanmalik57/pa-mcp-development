# ===========================================
# AUTHORS TABLE
# ===========================================
AUTHORS_TABLE = {
    "AUTH001": {
        "name": "Emily Carter",
        "email": "emily.carter@example.com",
        "nationality": "Canadian",
    },
    "AUTH002": {
        "name": "Daniel Rodriguez",
        "email": "daniel.rod@example.com",
        "nationality": "Spanish",
    },
    "AUTH003": {
        "name": "Harper Williams",
        "email": "harper.w@example.com",
        "nationality": "American",
    },
}

# ===========================================
# BOOKS TABLE (FOREIGN KEY: author_id → AUTHORS_TABLE)
# ===========================================
BOOKS_TABLE = {
    "BOOK100": {
        "title": "The Silent Forest",
        "author_id": "AUTH001",     # FK → AUTHORS_TABLE
        "genre": "Fantasy",
        "price": 14.99,
        "stock": 25,
    },
    "BOOK205": {
        "title": "Beyond the Horizon",
        "author_id": "AUTH003",     # FK → AUTHORS_TABLE
        "genre": "Science Fiction",
        "price": 19.50,
        "stock": 12,
    },
    "BOOK318": {
        "title": "Shadows of Yesterday",
        "author_id": "AUTH002",     # FK → AUTHORS_TABLE
        "genre": "Drama",
        "price": 11.75,
        "stock": 33,
    },
}

# ===========================================
# CUSTOMERS TABLE
# ===========================================
CUSTOMERS_TABLE = {
    "CUST700": {
        "name": "Liam Anderson",
        "email": "liam.anderson@example.com",
        "phone": "555-9012",
    },
    "CUST845": {
        "name": "Sophia Martinez",
        "email": "sophia.m@example.com",
        "phone": "555-4477",
    },
}

# ===========================================
# ORDERS TABLE
# (FOREIGN KEYS: customer_id → CUSTOMERS_TABLE,
#                 book_id → BOOKS_TABLE)
# ===========================================
ORDERS_TABLE = {
    "ORD9001": {
        "customer_id": "CUST700",    # FK → CUSTOMERS_TABLE
        "book_id": "BOOK100",        # FK → BOOKS_TABLE
        "quantity": 2,
        "price": 29.98,              # quantity * book price
        "date": "2024-01-15",
        "status": "Shipped",
    },
    "ORD9008": {
        "customer_id": "CUST845",
        "book_id": "BOOK205",
        "quantity": 1,
        "price": 19.50,
        "date": "2024-02-12",
        "status": "Processing",
    },
    "ORD9021": {
        "customer_id": "CUST700",
        "book_id": "BOOK318",
        "quantity": 3,
        "price": 35.25,
        "date": "2024-03-05",
        "status": "Delivered",
    },
}
