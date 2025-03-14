from src.backend.services.book import BookService


def get_books():
    service = BookService()

    books = service.get()

    return [
        book.to_dict(exclude = ["created_at","updated_at"])
        for book in books
    ]

def delete_book():
    pass