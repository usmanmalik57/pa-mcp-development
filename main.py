import asyncio
from fastmcp import FastMCP

# Import dummy database
from books_db import AUTHORS_TABLE, BOOKS_TABLE, CUSTOMERS_TABLE, ORDERS_TABLE

mcp = FastMCP(name="Bookstore MCP Server")

# ======================================================
# 1. GET BOOK BY TITLE
# ======================================================
@mcp.tool
async def get_book_by_title(title: str) -> dict | str:
    """Get detailed book information using a book title."""
    await asyncio.sleep(0.5)
    for book_id, book in BOOKS_TABLE.items():
        if title.lower() in book["title"].lower():
            return {
                "book_id": book_id,
                **book,
            }
    return f"No book found with title matching '{title}'."

# ======================================================
# 2. GET AUTHOR BY NAME
# ======================================================
@mcp.tool
async def get_author_by_name(name: str) -> dict | str:
    """Get author details using an author's full or partial name."""
    await asyncio.sleep(0.5)
    for author_id, author in AUTHORS_TABLE.items():
        if name.lower() in author["name"].lower():
            return {
                "author_id": author_id,
                **author,
            }
    return f"No author found matching '{name}'."

# ======================================================
# 3. GET CUSTOMER BY NAME
# ======================================================
@mcp.tool
async def get_customer_by_name(name: str) -> dict | str:
    """Get customer details by their full or partial name."""
    await asyncio.sleep(0.5)
    for customer_id, customer in CUSTOMERS_TABLE.items():
        if name.lower() in customer["name"].lower():
            return {
                "customer_id": customer_id,
                **customer,
            }
    return f"No customer found matching '{name}'."

# ======================================================
# 4. GET BOOKS WRITTEN BY A GIVEN AUTHOR
# ======================================================
@mcp.tool
async def get_books_by_author(author_name: str) -> list[dict] | str:
    """Return a list of books written by an author."""
    await asyncio.sleep(0.5)

    # Step 1: Find author_id
    matched_authors = [
        author_id
        for author_id, author in AUTHORS_TABLE.items()
        if author_name.lower() in author["name"].lower()
    ]

    if not matched_authors:
        return f"No author found matching '{author_name}'."

    author_id = matched_authors[0]

    # Step 2: Find all books with this author_id
    books = [
        {"book_id": bid, **book}
        for bid, book in BOOKS_TABLE.items()
        if book["author_id"] == author_id
    ]

    return books or f"No books found for author '{author_name}'."

# ======================================================
# 5. GET ALL ORDERS FOR A CUSTOMER
# ======================================================
@mcp.tool
async def get_orders_by_customer(customer_name: str) -> dict | str:
    """Return all order details for a given customer name."""
    await asyncio.sleep(0.5)

    # Find customer ID
    cust_id = None
    for cid, cust in CUSTOMERS_TABLE.items():
        if customer_name.lower() in cust["name"].lower():
            cust_id = cid
            break

    if not cust_id:
        return f"No customer found matching '{customer_name}'."

    # Collect orders
    orders = {
        oid: order for oid, order in ORDERS_TABLE.items()
        if order["customer_id"] == cust_id
    }

    return orders or f"No orders found for '{customer_name}'."

# ======================================================
# 6. GET TOTAL AMOUNT SPENT BY CUSTOMER
# ======================================================
@mcp.tool
async def get_total_spent_by_customer(customer_name: str) -> str:
    """Calculate the total amount spent by a customer."""
    await asyncio.sleep(0.5)

    # Find customer ID
    cust_id = None
    for cid, cust in CUSTOMERS_TABLE.items():
        if customer_name.lower() in cust["name"].lower():
            cust_id = cid
            break

    if not cust_id:
        return f"No customer found matching '{customer_name}'."

    total = 0.0
    for order in ORDERS_TABLE.values():
        if order["customer_id"] == cust_id:
            total += float(order["price"])

    return f"Customer '{customer_name}' has spent ${total:.2f} in total."

# ======================================================
# 7. GET ORDER DETAILS BY ORDER ID
# ======================================================
@mcp.tool
async def get_order_details(order_id: str) -> dict | str:
    """Get full details for a specific order."""
    await asyncio.sleep(0.5)

    order = ORDERS_TABLE.get(order_id)
    if not order:
        return f"No order found with ID '{order_id}'."

    # Attach book and customer details
    book_info = BOOKS_TABLE.get(order["book_id"], {})
    customer_info = CUSTOMERS_TABLE.get(order["customer_id"], {})

    return {
        "order_id": order_id,
        "order": order,
        "book": book_info,
        "customer": customer_info,
    }


# ======================================================
# 8. GET AUTHOR BY ID
# ======================================================
@mcp.tool
async def get_author_by_id(author_id: str) -> dict | str:
    """Retrieve full author details using their author ID."""
    await asyncio.sleep(0.5)

    author = AUTHORS_TABLE.get(author_id)
    if not author:
        return f"No author found with ID '{author_id}'."

    return {
        "author_id": author_id,
        **author,
    }


# RUN SERVER
if __name__ == "__main__":
    mcp.run()
