from bookshelf.models import Book

# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Check if it’s deleted
Book.objects.all()
# Output: <QuerySet []>