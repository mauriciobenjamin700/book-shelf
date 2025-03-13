from pytest import raises
from time import sleep

from src.backend.constants.messages.server import *
from src.backend.db.models import UserModel
from src.backend.db.repositories.user import UserRepository
from src.backend.schemas.user import (
    UserLogin,
    UserRegister,
    UserResponse
)


def test_UserRepository_update_success(mock_UserModel):
    
    # Arrange
    data = UserModel(**mock_UserModel.to_dict()) 
    
    login = UserLogin(
        email=mock_UserModel.email,
        password=mock_UserModel.password
    )
    
    update = UserRegister(
        username="new_username",
        email="email-new@gmai.com",
        password="new_passwordA123"
    )
    
    repository = UserRepository()
    
    repository.create(data)
    
    sleep(1)
    
    # Act
    
    user = repository.update(login, update)
    
    # Assert
    
    assert isinstance(user, UserResponse)
    assert user.id == data.id
    assert user.username == update.username
    assert user.email == update.email
    assert user.created_at == data.created_at
    assert user.updated_at != data.updated_at

    
    
    result = repository.delete(
        UserLogin(
            email=update.email,
            password=update.password
        )
    )
    
    assert result is True
    
    
def test_UserRepository_update_fail_invalid_input_login(mock_UserModel):
    
    # Arrange
    data = mock_UserModel
    repository = UserRepository()
    
    # Act
    
    with raises(ValueError) as exc:
        repository.update(data, mock_UserModel)
    
    # Assert
    
    assert str(exc.value) == ERROR_USER_REPOSITORY_GET_INPUT_TYPE
    
    
def test_UserRepository_update_fail_invalid_input_update(mock_UserModel):
    
    # Arrange
    data = UserModel(**mock_UserModel.to_dict()) 
    
    login = UserLogin(
        email=mock_UserModel.email,
        password="wrong_passwordA123"
    )
    
    repository = UserRepository()
    
    
    # Act
    
    with raises(ValueError) as exc:
        repository.update(login, data)
    
    # Assert
    
    assert str(exc.value) == ERROR_USER_REPOSITORY_UPDATE_INPUT_TYPE
    
