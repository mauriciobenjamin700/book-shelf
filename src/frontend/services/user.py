from src.backend.schemas.user import UserLogin, UserRegister
from src.backend.services.user import UserServices


def user_login(email: str , password: str):
    request = UserLogin(email = email, password = password)
    user_service = UserServices()
    response = user_service.login(request)
    return response
    
def user_register(name: str, email: str, password: str):
    """
    Create a new user account in the system
    
    - Args:
        - name: user name
        - email: user email
        - password: user password
    - Returns:
        - response: dict with the user information
    """
    request = UserRegister(username = name, email = email, password = password)
    user_service = UserServices()
    response = user_service.register(request)
    return response