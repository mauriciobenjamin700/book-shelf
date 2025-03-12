import pytest

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