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
    """

    def login(request: UserLogin) -> UserResponse:
        pass

    def register(request: UserRegister) -> UserResponse:
        pass
