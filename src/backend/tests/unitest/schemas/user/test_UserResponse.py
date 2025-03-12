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
    assert schema.name == data.get("name").upper()
    assert schema.email == data.get('email')



def test_UserResponse_fail_name_required(mock_UserResponse_data):

    # Arrange

    data = mock_UserResponse_data
    del data["name"]

    # Act

    with raises(ValidationError) as e:
        UserResponse(**data)

    # Assert
    
    assert e.value.field == "name"
    assert e.value.detail == ERROR_USER_REQUIRED_FIELD_NAME


def test_UserResponse_fail_name_type(mock_UserResponse_data):

    # Arrange

    data = mock_UserResponse_data
    data["name"] = 123

    # Act

    with raises(ValidationError) as e:
        UserResponse(**data)

    # Assert
    
    assert e.value.field == "name"
    assert e.value.detail == ERROR_NAME_INVALID_FORMAT_TYPE


def test_UserResponse_fail_name_minlength(mock_UserResponse_data):

    # Arrange

    data = mock_UserResponse_data
    data["name"] = "a"

    # Act

    with raises(ValidationError) as e:
        UserResponse(**data)

    # Assert
    
    assert e.value.field == "name"
    assert e.value.detail == ERROR_NAME_INVALID_FORMAT_MIN_LENGTH


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