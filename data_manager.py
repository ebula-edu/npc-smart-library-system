import json
import os

DATA_FILE = "data.json"

def load_data():
    """Load data from JSON file and return sorted list."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return sorted(data, key=lambda x: x["id"])
    except (json.JSONDecodeError, KeyError):
        return []

def save_data(data):
    """Save sorted data to JSON file."""
    sorted_data = sorted(data, key=lambda x: x["id"])
    with open(DATA_FILE, "w") as f:
        json.dump(sorted_data, f, indent=4)

def add_book(data, book):
    """Add a book and return updated sorted list."""
    data.append(book)
    return sorted(data, key=lambda x: x["id"])

def update_book(data, target_id, updated_fields):
    """Update a book's details."""
    for book in data:
        if book["id"] == target_id:
            book.update(updated_fields)
            break
    return data

def delete_book(data, target_id):
    """Remove a book by ID."""
    return [book for book in data if book["id"] != target_id]

