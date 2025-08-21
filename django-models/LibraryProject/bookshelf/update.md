from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Output
book
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
