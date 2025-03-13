from src.backend.constants.messages.server import (
    ERROR_USER_REPOSITORY_CREATE_INPUT_TYPE,
    ERROR_USER_REPOSITORY_GET_INPUT_TYPE,
    ERROR_USER_REPOSITORY_UPDATE_INPUT_TYPE
)
from src.backend.db.models import UserModel
from src.backend.db.settings.connection import DatabaseManager
from src.backend.schemas.user import (
    UserLogin,
    UserRegister,
    UserResponse
)
from src.backend.utils.generate import get_current_date
from src.backend.utils.security.password import (
    protect, 
    verify
)


class UserRepository:
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
        self.table_name = 'users'

    def create(self, data: UserModel) -> UserResponse:
        """
        Create a new user register in database

        - Args:
            - data: UserModel: User Data

        - Returns
            - UserResponse: User data after register
        """
        if not isinstance(data, UserModel):
            raise ValueError(ERROR_USER_REPOSITORY_CREATE_INPUT_TYPE)
        try:
            data.password = protect(data.password)
            
            id = data.id
            """
            update_time {
                seconds: 1741819898
                nanos: 156255000
            }
            """
            self.db.connection.collection(self.table_name).document(id).set(data.to_dict())
                    
            return UserResponse(**data.to_dict())
        
        except Exception as e:
            print(e)
            return None

    def get(self, data: UserLogin) -> UserResponse | None:
        """
        Get a user in database if the credentials are correct

        - Args:
            - data: UserLogin: Login credentials to get all user data

        - Returns:
            - UserResponse: If the credentials are correct, return respective user data
            - None: If the credentials are incorrect, return None
        """
        #response = self.db.connection.collection(self.table_name).where('email', '==', data.email).stream()
        
        if not isinstance(data, UserLogin):
            raise ValueError(ERROR_USER_REPOSITORY_GET_INPUT_TYPE)
        
        try:
            
            response = self.__get_reference(data.email).get()
            
            response = response.to_dict()
            
            if verify(data.password, response['password']):
            
                return UserResponse(**response)
            
            return None
        
        except Exception as e:
            print(e)
            return


    def update(self, login: UserLogin ,data: UserRegister) -> UserResponse | None:
        """
        Update user data on database, where email is the unique key and can't be updated

        - Args:
            - login: UserLogin: User credentials to get user reference
            - data: UserRegister: Usar data to update
        
        - Returns:
            - UserResponse: User data after update
        """
        if not isinstance(login, UserLogin):
            raise ValueError(ERROR_USER_REPOSITORY_GET_INPUT_TYPE)
        if not isinstance(data, UserRegister):
            raise ValueError(ERROR_USER_REPOSITORY_UPDATE_INPUT_TYPE)
        try:
            user_ref = self.__get_reference(login.email)
        
            user_ref.update({
                "username": data.username, 
                "email": data.email,
                "password": protect(data.password), 
                "updated_at": get_current_date()
            })
            
            return UserResponse(**user_ref.get().to_dict())
        
        except Exception as e:
            print(e)
            return None
        

    def delete(self, data: UserLogin) -> bool:
        """
        Delete user data on database

        - Args:
            - data: UserLogin
        """
        
        if not isinstance(data, UserLogin):
            raise ValueError(ERROR_USER_REPOSITORY_GET_INPUT_TYPE)
        
        try:
        
            user_ref = self.__get_reference(data.email)
            
            user_ref.delete()
        
            return True
        
        except:
        
            return False

        
    def __get_reference(self, email: str):
        """
        Get the user reference in database

        - Args:
            - email: str: User email

        - Returns:
            - DocumentReference: User reference in database
        """
        response = self.db.connection.collection(self.table_name).where('email', '==', email).stream()
        
        for doc in response:
            response = doc.reference
            break
        
        return response