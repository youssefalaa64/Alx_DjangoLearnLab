
from .models import Author, Book, Library, Librarian

# 1. Query all books by a specific author (e.g., "George Orwell")
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return f"No author found with name {author_name}"

# 2. List all books in a library (e.g., "Central Library")
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"

# 3. Retrieve the librarian for a library (e.g., "Central Library")
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # one-to-one reverse accessor
        return librarian
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"
    except Librarian.DoesNotExist:
        return f"No librarian assigned to {library_name}"

# === Sample Usage (if running in shell or script context) ===
if __name__ == '__main__':
    # These are examples — replace with real names from your database
    print("Books by George Orwell:")
    print(get_books_by_author("George Orwell"))

    print("\nBooks in Central Library:")
    print(get_books_in_library("Central Library"))

    print("\nLibrarian for Central Library:")
    print(get_librarian_for_library("Central Library"))