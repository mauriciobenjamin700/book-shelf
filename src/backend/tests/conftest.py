import pytest


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
        "name": "Tester",
        "email": "user@example.com",
        "password": "password1A-"
    }

@pytest.fixture
def mock_UserResponse_data():
    return {
        "id": "password1A-",
        "name": "Tester",
        "email": "user@example.com",
        
    }