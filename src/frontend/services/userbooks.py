from src.backend.schemas.book import BookRequest
from src.backend.services.book import BookService


def get_books():
    service = BookService()

    books = service.get()

    return [
        book.to_dict()
        for book in books
    ]

def register_book(title: str, author: str, pages: int, year:int):
    service = BookService()

    response = service.create(
        BookRequest(
            title=title,
            author=author,
            pages=int(pages),
            year=int(year)
        )
    )

    return response

def delete_book(id: str):
    
    service = BookService()
    service.delete(id)


def update_book(id: str, title: str, author: str, pages: int, year:int):

    service = BookService()
    service.update(
        id=id,
        request=BookRequest(
            title=title,
            author=author,
            pages=int(pages),
            year=int(year)
        )
    )