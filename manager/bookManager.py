from manager.objects.book import Book, Arthor, BookSchema

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def get_books(self) -> str:
        return BookSchema(many=True).dump(self.books)

book_manager_instance = BookManager()
book_manager_instance.add_book(Book(name="math", price=100, arthor=Arthor("newton")))