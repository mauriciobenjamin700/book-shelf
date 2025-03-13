from pytest import raises


from src.backend.constants.messages.user import *
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


def test_UserLogin_fail_email_required(mock_UserLogin_data):

    # Arrange

    data = mock_UserLogin_data
    del data["email"]

    # Act

    with raises(ValidationError) as e:
        UserLogin(**data)

    # Assert
    
    assert e.value.field == "email"
    assert e.value.detail == ERROR_USER_REQUIRED_FIELD_EMAIL


def test_UserLogin_fail_email_type(mock_UserLogin_data):

    # Arrange

    data = mock_UserLogin_data
    data["email"] = 12345

    # Act

    with raises(ValidationError) as e:
        UserLogin(**data)

    # Assert
    
    assert e.value.field == "email"
    assert e.value.detail == ERROR_EMAIL_INVALID_FORMAT_TYPE


def test_UserLogin_fail_email_type(mock_UserLogin_data):

    # Arrange

    data = mock_UserLogin_data
    data["email"] = "email.com"

    # Act

    with raises(ValidationError) as e:
        UserLogin(**data)

    # Assert
    
    assert e.value.field == "email"
    assert e.value.detail == ERROR_EMAIL_INVALID_FORMAT_MASK


def test_UserLogin_fail_password_required(mock_UserLogin_data):

    # Arrange

    data = mock_UserLogin_data
    del data["password"]

    # Act

    with raises(ValidationError) as e:
        UserLogin(**data)

    # Assert
    
    assert e.value.field == "password"
    assert e.value.detail == ERROR_USER_REQUIRED_FIELD_PASSWORD


def test_UserLogin_fail_password_type(mock_UserLogin_data):

    # Arrange

    data = mock_UserLogin_data
    data["password"] = 123

    # Act

    with raises(ValidationError) as e:
        UserLogin(**data)

    # Assert
    
    assert e.value.field == "password"
    assert e.value.detail == ERROR_PASSWORD_INVALID_FORMAT_TYPE


def test_UserLogin_fail_password_min_length(mock_UserLogin_data):

    # Arrange

    data = mock_UserLogin_data
    data["password"] = "1234"

    # Act

    with raises(ValidationError) as e:
        UserLogin(**data)

    # Assert
    
    assert e.value.field == "password"
    assert e.value.detail == ERROR_PASSWORD_INVALID_FORMAT_MIN_LENGTH


def test_UserLogin_fail_password_max_length(mock_UserLogin_data):

    # Arrange

    data = mock_UserLogin_data
    data["password"] = "1234"*255

    # Act

    with raises(ValidationError) as e:
        UserLogin(**data)

    # Assert
    
    assert e.value.field == "password"
    assert e.value.detail == ERROR_PASSWORD_INVALID_FORMAT_MAX_LENGTH


def test_UserLogin_fail_password_no_digit(mock_UserLogin_data):

    # Arrange

    data = mock_UserLogin_data
    data["password"] = "abcdefgh"

    # Act

    with raises(ValidationError) as e:
        UserLogin(**data)

    # Assert
    
    assert e.value.field == "password"
    assert e.value.detail == ERROR_PASSWORD_INVALID_FORMAT_DIGIT


def test_UserLogin_fail_password_no_lowercase(mock_UserLogin_data):

    # Arrange

    data = mock_UserLogin_data
    data["password"] = "ABCDEFGH1"

    # Act

    with raises(ValidationError) as e:
        UserLogin(**data)

    # Assert
    
    assert e.value.field == "password"
    assert e.value.detail == ERROR_PASSWORD_INVALID_FORMAT_LOWERCASE


def test_UserLogin_fail_password_no_uppercase(mock_UserLogin_data):

    # Arrange

    data = mock_UserLogin_data
    data["password"] = "abcdefgh1"

    # Act

    with raises(ValidationError) as e:
        UserLogin(**data)

    # Assert
    
    assert e.value.field == "password"
    assert e.value.detail == ERROR_PASSWORD_INVALID_FORMAT_UPPERCASE


def test_UserLogin_fail_password_no_especial(mock_UserLogin_data):

    # Arrange

    data = mock_UserLogin_data
    data["password"] = "abcdefghA1"

    # Act

    with raises(ValidationError) as e:
        UserLogin(**data)

    # Assert
    
    assert e.value.field == "password"
    assert e.value.detail == ERROR_PASSWORD_INVALID_FORMAT_SPECIAL_CHARACTER