from src.backend.schemas.user import (
    UserDB,
    UserLogin,
    UserRegister,
    UserResponse
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

    def create(data: UserDB) -> UserResponse:
        """
        Create a new user register in database

        - Args:
            - data: UserDB: User Data

        - Returns
            - UserResponse: User data after register
        """
        pass

    def get(data: UserLogin) -> UserResponse | None:
        """
        Get a user in database if the credentials are correct

        - Args:
            - data: UserLogin: Login credentials to get all user data

        - Returns:
            - UserResponse: If the credentials are correct, return respective user data
            - None: If the credentials are incorrect, return None
        """
        pass

    def update(data: UserRegister) -> UserResponse:
        """
        Update user data on database

        - Args:
            - data: UserRegister: Usar data to update
        
        - Returns:
            - UserResponse: User data after update
        """
        pass

    def delete(data: UserLogin) -> bool:
        """
        Delete user data on database

        - Args:
            - data: UserLogin
        """
        pass