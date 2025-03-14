from src.backend.services.book import BookService


def get_books():
    service = BookService()

    books = service.get()

    return [
        book.to_dict()
        for book in books
    ]

def delete_book():
    pass