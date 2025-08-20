from bookshelf.models import Book

# Retrieve all books
books = Book.objects.get()
for b in books:
    print(b.title, b.author, b.publication_year)

# Output
# 1984 George Orwell 1949
