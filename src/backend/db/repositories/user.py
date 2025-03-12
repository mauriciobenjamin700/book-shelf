from src.backend.schemas.user import (
    UserDB,
    UserLogin,
    UserRegister,
    UserResponse
)
from src.backend.db.settings.connection import DatabaseManager
from src.backend.utils.generate import get_current_date
from src.backend.utils.security.password import protect, verify


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

    def create(self, data: UserDB) -> UserResponse:
        """
        Create a new user register in database

        - Args:
            - data: UserDB: User Data

        - Returns
            - UserResponse: User data after register
        """
        
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
        
        response = self.__get_reference(data.email).get()
        
        response = response.to_dict()
        
        if verify(data.password, response['password']):
        
            return UserResponse(**response)
        
        return None

    def update(self, data: UserRegister) -> UserResponse | None:
        """
        Update user data on database

        - Args:
            - data: UserRegister: Usar data to update
        
        - Returns:
            - UserResponse: User data after update
        """
        
        user_ref = self.__get_reference(data.email)
        
        user_ref.update({"username": data.username, "password": protect(data.password), "updated_at": get_current_date()})   
        

    def delete(self, data: UserLogin) -> bool:
        """
        Delete user data on database

        - Args:
            - data: UserLogin
        """
        
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