from src.backend.constants.messages.server import (
    ERROR_SERVER,
    ERROR_USER_REPOSITORY_GET_INPUT_TYPE,
    ERROR_USER_REPOSITORY_UPDATE_INPUT_TYPE,
)
from src.backend.constants.messages.user import (
    ERROR_USER_ALREADY_EXISTS,
    ERROR_USER_NOT_FOUND
)
from src.backend.db.models import UserModel
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
        """
        Login a user with email and password

        - Args:
            - request: UserLogin: User credentials

        - Returns:
            - UserResponse: User data

        - Raises:
            - RequestError
                - 404 - ERROR_USER_NOT_FOUND
            - ValidationError
                - request - INPUT TYPE
        """
        try:
            if not isinstance(request, UserLogin):
                raise ValidationError("request", ERROR_USER_REPOSITORY_GET_INPUT_TYPE)
            
            user = self.__repo.get(request)
            
            if not user:
                raise RequestError(404, ERROR_USER_NOT_FOUND)
            
            return user
            
        except RequestError as e:
            print(e)
            raise e
        
        except ValidationError as e:
            print(e)
            raise e
            
        except Exception as e:
            print(e)
            raise RequestError(500, ERROR_SERVER)

    def register(self, request: UserRegister) -> UserResponse:
        """
        Register a new user on the database.

        - Args:
            - request: UserLogin: User credentials

        - Returns:
            - UserResponse: User data

        - Raises:
            - RequestError
                - 404 - ERROR_USER_ALREADY_EXISTS
            - ValidationError
                - request - INPUT TYPE
        """
        try:
            if not isinstance(request, UserRegister):
                raise ValidationError("request", ERROR_USER_REPOSITORY_UPDATE_INPUT_TYPE)
            
            user_on_db = self.__repo.get(
                UserLogin(
                    email=request.email,
                    password=request.password,
                )
            )

            if user_on_db:
                raise RequestError(409, ERROR_USER_ALREADY_EXISTS)
            
            to_db = UserModel(
                username=request.username,
                email=request.email,
                password=request.password,
            )

            user = self.__repo.create(to_db)
            
            return user
        
        except RequestError as e:
            print(e)
            raise e
            
        except ValidationError as e:
            print(e)
            raise e
            
        except Exception as e:
            print(e)
            raise RequestError(500, ERROR_SERVER)
