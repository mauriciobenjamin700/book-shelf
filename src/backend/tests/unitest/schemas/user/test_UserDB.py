from pytest import raises


from src.backend.constants.messages.user import *
from src.backend.schemas.user import UserDB
from src.backend.schemas.settings.base import ValidationError


def test_UserDB_success(mock_UserRegister_data):
    
    #  Arrange

    data = mock_UserRegister_data

    # Act

    schema = UserDB(**data)

    # Assert
    
    assert isinstance(schema.id, str)
    assert schema.name == data.get("name").upper()
    assert schema.email == data.get('email')
    assert schema.password == data.get('password')
    assert isinstance(schema.created_at, str)
    assert isinstance(schema.updated_at, str)


def test_UserDB_fail_name_required(mock_UserRegister_data):

    # Arrange

    data = mock_UserRegister_data
    del data["name"]

    # Act

    with raises(ValidationError) as e:
        UserDB(**data)

    # Assert
    
    assert e.value.field == "name"
    assert e.value.detail == ERROR_USER_REQUIRED_FIELD_NAME


def test_UserDB_fail_name_type(mock_UserRegister_data):

    # Arrange

    data = mock_UserRegister_data
    data["name"] = 123

    # Act

    with raises(ValidationError) as e:
        UserDB(**data)

    # Assert
    
    assert e.value.field == "name"
    assert e.value.detail == ERROR_NAME_INVALID_FORMAT_TYPE


def test_UserDB_fail_name_minlength(mock_UserRegister_data):

    # Arrange

    data = mock_UserRegister_data
    data["name"] = "a"

    # Act

    with raises(ValidationError) as e:
        UserDB(**data)

    # Assert
    
    assert e.value.field == "name"
    assert e.value.detail == ERROR_NAME_INVALID_FORMAT_MIN_LENGTH


def test_UserDB_fail_email_required(mock_UserRegister_data):

    # Arrange

    data = mock_UserRegister_data
    del data["email"]

    # Act

    with raises(ValidationError) as e:
        UserDB(**data)

    # Assert

    assert e.value.field == "email"
    assert e.value.detail == ERROR_USER_REQUIRED_FIELD_EMAIL


def test_UserDB_fail_email_type(mock_UserRegister_data):

    # Arrange

    data = mock_UserRegister_data
    data["email"] = 12345

    # Act

    with raises(ValidationError) as e:
        UserDB(**data)

    # Assert
    
    assert e.value.field == "email"
    assert e.value.detail == ERROR_EMAIL_INVALID_FORMAT_TYPE


def test_UserDB_fail_email_type(mock_UserRegister_data):

    # Arrange

    data = mock_UserRegister_data
    data["email"] = "email.com"

    # Act

    with raises(ValidationError) as e:
        UserDB(**data)

    # Assert
    
    assert e.value.field == "email"
    assert e.value.detail == ERROR_EMAIL_INVALID_FORMAT_MASK


def test_UserDB_fail_password_required(mock_UserRegister_data):

    # Arrange

    data = mock_UserRegister_data
    del data["password"]

    # Act

    with raises(ValidationError) as e:
        UserDB(**data)

    # Assert
    
    assert e.value.field == "password"
    assert e.value.detail == ERROR_USER_REQUIRED_FIELD_PASSWORD


def test_UserDB_fail_password_type(mock_UserRegister_data):

    # Arrange

    data = mock_UserRegister_data
    data["password"] = 123

    # Act

    with raises(ValidationError) as e:
        UserDB(**data)

    # Assert
    
    assert e.value.field == "password"
    assert e.value.detail == ERROR_PASSWORD_INVALID_FORMAT_TYPE


def test_UserDB_fail_password_min_length(mock_UserRegister_data):

    # Arrange

    data = mock_UserRegister_data
    data["password"] = "1234"

    # Act

    with raises(ValidationError) as e:
        UserDB(**data)

    # Assert
    
    assert e.value.field == "password"
    assert e.value.detail == ERROR_PASSWORD_INVALID_FORMAT_MIN_LENGTH


def test_UserDB_fail_password_max_length(mock_UserRegister_data):

    # Arrange

    data = mock_UserRegister_data
    data["password"] = "1234"*255

    # Act

    with raises(ValidationError) as e:
        UserDB(**data)

    # Assert
    
    assert e.value.field == "password"
    assert e.value.detail == ERROR_PASSWORD_INVALID_FORMAT_MAX_LENGTH


def test_UserDB_fail_password_no_digit(mock_UserRegister_data):

    # Arrange

    data = mock_UserRegister_data
    data["password"] = "abcdefgh"

    # Act

    with raises(ValidationError) as e:
        UserDB(**data)

    # Assert
    
    assert e.value.field == "password"
    assert e.value.detail == ERROR_PASSWORD_INVALID_FORMAT_DIGIT


def test_UserDB_fail_password_no_lowercase(mock_UserRegister_data):

    # Arrange

    data = mock_UserRegister_data
    data["password"] = "ABCDEFGH1"

    # Act

    with raises(ValidationError) as e:
        UserDB(**data)

    # Assert
    
    assert e.value.field == "password"
    assert e.value.detail == ERROR_PASSWORD_INVALID_FORMAT_LOWERCASE


def test_UserDB_fail_password_no_uppercase(mock_UserRegister_data):

    # Arrange

    data = mock_UserRegister_data
    data["password"] = "abcdefgh1"

    # Act

    with raises(ValidationError) as e:
        UserDB(**data)

    # Assert
    
    assert e.value.field == "password"
    assert e.value.detail == ERROR_PASSWORD_INVALID_FORMAT_UPPERCASE


def test_UserDB_fail_password_no_especial(mock_UserRegister_data):

    # Arrange

    data = mock_UserRegister_data
    data["password"] = "abcdefghA1"

    # Act

    with raises(ValidationError) as e:
        UserDB(**data)

    # Assert
    
    assert e.value.field == "password"
    assert e.value.detail == ERROR_PASSWORD_INVALID_FORMAT_SPECIAL_CHARACTER