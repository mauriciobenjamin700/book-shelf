from pytest import raises

from src.backend.constants.messages.server import ERROR_USER_REPOSITORY_GET_INPUT_TYPE
from src.backend.constants.messages.user import *
from src.backend.db.repositories.user import UserRepository
from src.backend.db.models import UserModel
from src.backend.schemas.settings.base import RequestError, ValidationError
from src.backend.schemas.user import UserLogin, UserResponse
from src.backend.services.user import UserServices



def test_UserService_login(mock_UserModel, mock_UserLogin_data):

    # Arrange
    data_db = UserModel(**mock_UserModel.to_dict())
    request = UserLogin(**mock_UserLogin_data.to_dict())
    service = UserServices()
    repository = UserRepository()

    user_db = repository.create(data_db)

    # Act

    response = repository.login(request)

    # Assert

    assert isinstance(response, UserResponse)
    assert response.id == user_db.id
    assert response.username == user_db.username
    assert response.email == request.email
    assert response.created_at == user_db.created_at

    repository.delete(
        UserLogin(
            email=mock_UserModel.email,
            password=mock_UserModel.password,
        )
    )


def test_UserService_login_invalid_input(mock_UserLogin_data):
    # Arrange

    request = mock_UserLogin_data.to_dict()
    repository = UserServices()

    # Act

    with raises(ValidationError) as e:
        repository.login(request)

    # Assert

    assert e.value.field == "request"
    assert e.value.detail == ERROR_USER_REPOSITORY_GET_INPUT_TYPE



def test_UserService_login_not_found(mock_UserRegister_data):
    # Arrange

    data_db = UserModel(**mock_UserRegister_data.to_dict())
    request = UserLogin(
        email=mock_UserRegister_data.email,
        password="wrong_password",
    )
    service = UserServices()
    repository = UserRepository()

    user_db = repository.create(data_db)

    # Act

    with raises(RequestError) as e:
        repository.login(request)

    # Assert

    assert e.value.code == 404
    assert e.value.detail == ERROR_USER_NOT_FOUND

    repository.delete(
        UserLogin(
            email=mock_UserRegister_data.email,
            password=mock_UserRegister_data.password,
        )
    )