from pytest import raises


from src.backend.schemas.user import UserLogin
from src.backend.schemas.settings.base import ValidationError


def test_UserLogin_success(mock_UserLogin_data):
    
    #  Arrange

    data = mock_UserLogin_data

    # Act

    schema = UserLogin(**data)

    # Assert

    assert schema.email == data.get('email')
    assert schema.password == data.get('password')