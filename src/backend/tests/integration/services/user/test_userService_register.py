from pytest import raises

from src.backend.constants.messages.server import ERROR_USER_REPOSITORY_GET_INPUT_TYPE, ERROR_USER_REPOSITORY_UPDATE_INPUT_TYPE
from src.backend.constants.messages.user import *
from src.backend.db.repositories.user import UserRepository
from src.backend.db.models import UserModel
from src.backend.schemas.settings.base import RequestError, ValidationError
from src.backend.schemas.user import UserLogin, UserRegister, UserResponse
from src.backend.services.user import UserServices



def test_UserService_register(mock_UserRegister):

    # Arrange
    request = UserRegister(**mock_UserRegister.to_dict())
    service = UserServices()
    repository = UserRepository()

    # Act

    response = service.register(request)

    # Assert

    assert isinstance(response, UserResponse)
    assert response.username == request.username
    assert response.email == request.email

    repository.delete(
        UserLogin(
            email=mock_UserRegister.email,
            password=mock_UserRegister.password,
        )
    )


def test_UserService_register_invalid_input(mock_UserLogin_data):
    # Arrange

    request = mock_UserLogin_data.copy()
    repository = UserServices()

    # Act

    with raises(ValidationError) as e:
        repository.register(request)

    # Assert

    assert e.value.field == "request"
    assert e.value.detail == ERROR_USER_REPOSITORY_UPDATE_INPUT_TYPE


def test_UserService_register_conflict(mock_UserRegister):
    # Arrange

    request = UserRegister(**mock_UserRegister.to_dict())
    service = UserServices()
    repository = UserRepository()
    
    model = UserModel(**mock_UserRegister.to_dict())

    user_db = repository.create(model)

    # Act

    with raises(RequestError) as e:
        service.register(request)

    # Assert

    assert e.value.status_code == 409
    assert e.value.detail == ERROR_USER_ALREADY_EXISTS

    repository.delete(
        UserLogin(
            email=mock_UserRegister.email,
            password=mock_UserRegister.password,
        )
    )