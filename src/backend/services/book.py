from src.backend.constants.messages.book import (
    ERROR_BOOK_ADD, 
    ERROR_BOOK_NOT_FOUND,
    ERROR_BOOKS_NOT_FOUND
)
from src.backend.constants.messages.server import ERROR_BOOK_REPOSITORY_BOOK_REQUEST_INPUT_TYPE, ERROR_SERVER
from src.backend.db.models import BookModel
from src.backend.db.repositories.book import BookRepository
from src.backend.schemas.book import (
    BookRequest, 
    BookFilters, BookResponse
)
from src.backend.schemas.settings.base import (
    RequestError,
    ValidationError
)


class BookService:
    """
    Class to manage the business logic of the book entity
    
    - methods:
        - create: Create a book
        - get: Get a book
        - update: Update a book
        - delete: Delete a book
    
    """
    def __init__(self):
        self.__repo = BookRepository()
        
        
    def create(self, request: BookRequest) -> BookResponse:
        """
        Create a book on the database
        
        - Args:
            - request: BookRequest
            
        - Returns:
            - BookResponse: The book created on the database
        """
        try:
            if not isinstance(request, BookRequest):
                
                raise ValidationError("request", ERROR_BOOK_REPOSITORY_BOOK_REQUEST_INPUT_TYPE)
            
            model_on_db = self.__repo.get(
                BookFilters(
                    **request.to_dict()
                )
            )
            
            if model_on_db:
                raise RequestError(409, ERROR_BOOK_ADD)
            
            model = BookModel(**request.to_dict())
            
            
            book = self.__repo.create(model)
            
            return book
        
        except RequestError as e:
            print(e)
            raise e
        
        except ValidationError as e:
            print(e)
            raise e
        
        except Exception as e:
            print(e)
            raise RequestError(500, ERROR_SERVER)
        

    def get(self, filters: BookFilters | None = None) -> list[BookResponse]:
        """
        Get a list of books from the database
        
        - Args:
            - filters: BookFilters
            
        - Returns:
            - list[BookResponse]: A list of books
        """
        try:
            
            book = self.__repo.get(filters)
            
            if not book:
                raise RequestError(404, ERROR_BOOKS_NOT_FOUND)
            
            return book
        
        except RequestError as e:
            print(e)
            raise e
        
        except ValidationError as e:
            print(e)
            raise e
        
        except Exception as e:
            print(e)
            raise RequestError(500, ERROR_SERVER)
            
    def update(self, id: str, request: BookRequest) -> BookResponse:
        """
        Update a book on the database   
        
        - Args:
            - id: str = The id of the book
            - request: BookRequest: new data for the book
            
        - Returns:
            - BookResponse: The book updated on the database
        """
        try:
            
            if not isinstance(request, BookRequest):
                raise ValidationError("request", ERROR_BOOK_REPOSITORY_BOOK_REQUEST_INPUT_TYPE)
            
            book_on_db = self.__repo.get_by_id(id)
            
            if not book_on_db:
                raise RequestError(404, ERROR_BOOK_NOT_FOUND)
            
            book = self.__repo.update(id, request)
            
            return book
            
        except RequestError as e:
            print(e)
            raise e
        
        except ValidationError as e:
            print(e)
            raise e
        
        except Exception as e:
            print(e)
            raise RequestError(500, ERROR_SERVER)
            
    def delete(self, id: str) -> None:
        """
        Delete a book from the database
        
        - Args:
            - id: str = The id of the book
        
        - Returns:
            - None
        """
        try:
            
            result = self.__repo.delete(id)
            
            if not result:
                raise RequestError(404, ERROR_BOOK_NOT_FOUND)
    
            
        except RequestError as e:
            print(e)
            raise e
        
        except ValidationError as e:
            print(e)
            raise e
        
        except Exception as e:
            print(e)
            raise RequestError(500, ERROR_SERVER)