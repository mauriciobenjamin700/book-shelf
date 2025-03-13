import pytest

from src.backend.db.models import *
from src.backend.schemas.user import *
from src.backend.utils.generate import get_current_date


######################## Data

@pytest.fixture
def mock_UserLogin_data():
    return {
        "email": "user@example.com",
        "password": "password1A-"
    }

@pytest.fixture
def mock_UserRegister_data():
    return {
        "username": "Tester",
        "email": "user@example.com",
        "password": "password1A-"
    }

@pytest.fixture
def mock_UserResponse_data():
    return {
        "id": "password1A-",
        "username": "Tester",
        "email": "user@example.com",
        "created_at": get_current_date(),
        "updated_at": get_current_date()
        
    }
    
    
######################## Schemas

@pytest.fixture
def mock_UserModel(mock_UserRegister_data):
    return UserModel(
        **mock_UserRegister_data
    )

@pytest.fixture
def mock_UserLogin(mock_UserLogin_data):
    return UserLogin(
        **mock_UserLogin_data
    )
    
@pytest.fixture
def mock_UserRegister(mock_UserRegister_data):
    return UserRegister(
        **mock_UserRegister_data
    )