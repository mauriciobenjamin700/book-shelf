from src.backend.constants.messages.server import (
    ERROR_BOOK_REPOSITORY_CREATE_INPUT_TYPE,
    ERROR_BOOK_REPOSITORY_GET_INPUT_TYPE
)
from src.backend.db.models import BookModel
from src.backend.db.settings.connection import DatabaseManager
from src.backend.schemas.book import (
    BookFilters,
    BookRequest,
    BookResponse
)
from src.backend.utils.generate import get_current_date
from src.backend.utils.security.password import (
    protect, 
    verify
)


class BookRepository:
    """
    Class to manager database operations to user table.

    - Methods:
        - create
        - get
        - update
        - delete
    """
    def __init__(self):
        self.db = DatabaseManager()
        self.db.connect()
        self.table_name = 'books'

    def create(self, data: BookModel) -> BookResponse:
        """
        Create a new user register in database

        - Args:
            - data: BookModel: Book Data

        - Returns
            - BookResponse: Book data after register
        """
        if not isinstance(data, BookModel):
            raise ValueError(ERROR_BOOK_REPOSITORY_CREATE_INPUT_TYPE)
        try:
            
            id = data.id
            """
            update_time {
                seconds: 1741819898
                nanos: 156255000
            }
            """
            self.db.connection.collection(self.table_name).document(id).set(data.to_dict())
                    
            return BookResponse(**data.to_dict())
        
        except Exception as e:
            print(e)
            return None

    def get(self, filters: BookFilters | None) -> list[BookResponse]:
        """
        Get a user in database if the credentials are correct

        - Args:
            - data: BookLogin: Login credentials to get all user data

        - Returns:
            - BookResponse: If the credentials are correct, return respective user data
            - None: If the credentials are incorrect, return None
        """
        #response = self.db.connection.collection(self.table_name).where('email', '==', data.email).stream()
        
        if filters:
            if not isinstance(filters, BookFilters):
                raise ValueError(ERROR_BOOK_REPOSITORY_GET_INPUT_TYPE)
        
        try:
            query = self.db.connection.collection(self.table_name)
            
            if filters:
                if not isinstance(filters, BookFilters):
                    raise ValueError(ERROR_BOOK_REPOSITORY_GET_INPUT_TYPE)
                
                if filters.title:
                    query = query.where('title', '==', filters.title)
                    
                if filters.author:
                    query = query.where('author', '==', filters.author)
                    
                if filters.pages:
                    query = query.where('pages', '==', filters.pages)
                    
                if filters.year:
                    query = query.where('year', '==', filters.year)


            response = query.stream()
            
            books = [BookResponse(**doc.to_dict()) for doc in response]
            
            return books

        except Exception as e:
            print(e)
            return []
        
    def get_by_id(self, id: str) -> BookResponse | None:
        """
        Get a user in database if the credentials are correct

        - Args:
            - data: BookLogin: Login credentials to get all user data

        - Returns:
            - BookResponse: If the credentials are correct, return respective user data
            - None: If the credentials are incorrect, return None
        """
        #response = self.db.connection.collection(self.table_name).where('email', '==', data.email).stream()
        
        try:
            query = self.db.connection.collection(self.table_name)
            
            response = query.where('id', '==', id).stream()
            
            for doc in response:
                return BookResponse(**doc.to_dict())
            
            return None

        except Exception as e:
            print(e)
            return


    def update(self, id: str , new_data: BookRequest) -> BookResponse | None:
        """
        Update user data on database, where email is the unique key and can't be updated

        - Args:
            - login: BookLogin: Book credentials to get user reference
            - data: BookRegister: Usar data to update
        
        - Returns:
            - BookResponse: Book data after update
        """
        if not isinstance(new_data, BookRequest):
            raise ValueError(ERROR_BOOK_REPOSITORY_BOOK_REQUEST_INPUT_TYPE)
        try:
            user_ref = self.__get_reference(id)
        
            user_ref.update({
                "title": new_data.title, 
                "author": new_data.author,
                "pages": new_data.pages,
                "year": new_data.year,
                "updated_at": get_current_date()
            })
            
            return BookResponse(**user_ref.get().to_dict())
        
        except Exception as e:
            print(e)
            return None
        

    def delete(self, id: str) -> bool:
        """
        Delete user data on database

        - Args:
            - id: str: Book id
        
        - Returns:
            - bool: If the user was deleted, return True, else return False
        """
        
        try:
        
            user_ref = self.__get_reference(id)
            
            user_ref.delete()
        
            return True
        
        except:
        
            return False

        
    def __get_reference(self, id: str):
        """
        Get the user reference in database

        - Args:
            - email: str: Book email

        - Returns:
            - DocumentReference: Book reference in database
        """
        response = self.db.connection.collection(self.table_name).where('id', '==', id).stream()
        
        for doc in response:
            response = doc.reference
            break
        
        return response