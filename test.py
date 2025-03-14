"""
This file is used to test the service layer of the application.
"""

from src.backend.schemas.book import BookRequest
from src.backend.services.book import BookService


service = BookService()

response = service.create(
    BookRequest(
        title="The Hobbit",
        author="J.R.R. Tolkien",
        pages=310,
        year=1937
    )
)

print(response)

response = service.create(
    BookRequest(
        title="The Lord of the Rings",
        author="J.R.R. Tolkien",
        pages=1,
        year=1954
    )
)

print(response)


response = service.create(
    BookRequest(
        title="Dom Casmurro",
        author="Machado de Assis",
        pages=3,
        year=1899
    )
)

print(response)