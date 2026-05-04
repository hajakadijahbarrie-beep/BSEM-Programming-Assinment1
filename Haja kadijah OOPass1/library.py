import asyncio
from typing import Dict, List


# Simulated database of books
books: Dict[int, Dict[str, object]] = {
    101: {
        "id": 101,
        "title": "Introduction to Python",
        "author": "John Doe",
        "category": "Programming",
        "available": True
    },
    102: {
        "id": 102,
        "title": "Database Systems",
        "author": "Jane Smith",
        "category": "Computing",
        "available": True
    }
}


# Simulated database of users
users: Dict[int, Dict[str, object]] = {}

# Loan records storage
loans: List[Dict[str, object]] = []

# POST /users (create user)
async def create_user(user_id: int, name: str, email: str, user_type: str) -> str:
    print(f"Creating user {name}...")

    await asyncio.sleep(5)

    users[user_id] = {
        "id": user_id,
        "name": name,
        "email": email,
        "type": user_type
    }

    return f"User created successfully! ID = {user_id}"


# GET /users (get all users)
async def get_users() -> List[Dict[str, object]]:
    print("Retrieving all users...")

    await asyncio.sleep(3)

    return list(users.values())


# PATCH /books (update book)
async def update_book(book_id: int, new_title: str = None, new_author: str = None) -> str:
    print(f"Updating book {book_id}...")

    await asyncio.sleep(4)

    book = books.get(book_id)

    if book is None:
        return "Book not found"

    if new_title:
        book["title"] = new_title

    if new_author:
        book["author"] = new_author

    return f"Book {book_id} updated successfully"


# GET /loans
async def get_loans() -> List[Dict[str, object]]:
    print("Fetching all loan records...")

    await asyncio.sleep(3)

    return loans


# Simulating multiple users
async def main() -> None:
    print("Task 1 starting (Create User)")
    print("Task 2 starting (Update Book)")
    print("Task 3 starting (Get Loans)")

    results = await asyncio.gather(
        create_user(1, "Alice", "alice@email.com", "student"),
        update_book(101, new_title="Python Basics"),
        get_loans()
    )

    print("\n--- TASKS COMPLETED ---")

    print("\n--- RESULTS ---")
    for result in results:
        print(result)


asyncio.run(main())