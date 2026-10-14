from book import Book

book = Book()

book.set_title("Sample Book")
print("Output:")
print(f"Title: {book.get_title()}")
print()

book.set_number_of_pages(300)
print("Output:")
print(f"Number of Pages: {book.get_number_of_pages()}")
print()

book.set_is_fictional(True)
print("Output:")
print(f"Is Fictional: {book.get_is_fictional()}")
print()

print("Output:")
book.display()
