from src.backend.schemas.user import UserLogin
from src.backend.services.user import UserServices


def user_login(email: str , password: str):
    request = UserLogin(email = email, password = password)
    user_service = UserServices()
    response = user_service.login(request)
    return response
    
