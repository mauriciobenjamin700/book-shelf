from src.backend.constants.messages.user import (
    ERROR_USER_NOT_FOUND
)
from src.backend.db.repositories.user import UserRepository
from src.backend.schemas.settings.base import (
    RequestError,
    ValidationError
)
from src.backend.schemas.user import (
    UserLogin,
    UserRegister,
    UserResponse
)


class UserServices:
    """
    Methods:
        - login
        - register
        
    - Raises:
        - RequestError
        - ValidationError
    """
    def __init__(self):
        self.__repo = UserRepository()

    def login(self, request: UserLogin) -> UserResponse:
        try:
            user = self.__repo.get(request)
            
            if not user:
                raise RequestError(ERROR_USER_NOT_FOUND)
            
            return user
            
        except RequestError as e:
            print(e)
            raise e
        
        except ValidationError as e:
            print(e)
            raise e
            
        except Exception as e:
            print(e)
            raise RequestError(500, "Internal Server Error")

    def register(request: UserRegister) -> UserResponse:
        pass
