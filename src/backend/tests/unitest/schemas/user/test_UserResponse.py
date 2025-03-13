from pytest import raises


from src.backend.constants.messages.user import *
from src.backend.schemas.user import UserResponse
from src.backend.schemas.settings.base import ValidationError


def test_UserResponse_success(mock_UserResponse_data):
    
    #  Arrange

    data = mock_UserResponse_data

    # Act

    schema = UserResponse(**data)

    # Assert
    
    assert schema.id == data.get("id")
    assert schema.username == data.get("username").upper()
    assert schema.email == data.get('email')
    assert schema.created_at == data.get("created_at")
    assert schema.created_at == data.get("updated_at")



def test_UserResponse_fail_username_required(mock_UserResponse_data):

    # Arrange

    data = mock_UserResponse_data
    del data["username"]

    # Act

    with raises(ValidationError) as e:
        UserResponse(**data)

    # Assert
    
    assert e.value.field == "username"
    assert e.value.detail == ERROR_USER_REQUIRED_FIELD_USERNAME


def test_UserResponse_fail_username_type(mock_UserResponse_data):

    # Arrange

    data = mock_UserResponse_data
    data["username"] = 123

    # Act

    with raises(ValidationError) as e:
        UserResponse(**data)

    # Assert
    
    assert e.value.field == "username"
    assert e.value.detail == ERROR_USERNAME_INVALID_FORMAT_TYPE


def test_UserResponse_fail_username_minlength(mock_UserResponse_data):

    # Arrange

    data = mock_UserResponse_data
    data["username"] = "a"

    # Act

    with raises(ValidationError) as e:
        UserResponse(**data)

    # Assert
    
    assert e.value.field == "username"
    assert e.value.detail == ERROR_USERNAME_INVALID_FORMAT_MIN_LENGTH


def test_UserResponse_fail_email_required(mock_UserResponse_data):

    # Arrange

    data = mock_UserResponse_data
    del data["email"]

    # Act

    with raises(ValidationError) as e:
        UserResponse(**data)

    # Assert

    assert e.value.field == "email"
    assert e.value.detail == ERROR_USER_REQUIRED_FIELD_EMAIL


def test_UserResponse_fail_email_type(mock_UserResponse_data):

    # Arrange

    data = mock_UserResponse_data
    data["email"] = 12345

    # Act

    with raises(ValidationError) as e:
        UserResponse(**data)

    # Assert
    
    assert e.value.field == "email"
    assert e.value.detail == ERROR_EMAIL_INVALID_FORMAT_TYPE


def test_UserResponse_fail_email_type(mock_UserResponse_data):

    # Arrange

    data = mock_UserResponse_data
    data["email"] = "email.com"

    # Act

    with raises(ValidationError) as e:
        UserResponse(**data)

    # Assert
    
    assert e.value.field == "email"
    assert e.value.detail == ERROR_EMAIL_INVALID_FORMAT_MASK