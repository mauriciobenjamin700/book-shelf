import pytest


######################## Data

@pytest.fixture
def mock_UserLogin_data():
    return {
        "email": "user@example.com",
        "password": "password1A-"
    }