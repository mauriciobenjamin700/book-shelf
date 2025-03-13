from pytest import raises

from src.backend.constants.messages.server import *
from src.backend.db.models import UserModel
from src.backend.db.repositories.user import UserRepository
from src.backend.schemas.user import (
    UserLogin,
    UserResponse
)


def test_UserRepository_get_success(mock_UserModel):
    
    # Arrange
    data = UserModel(**mock_UserModel.to_dict()) 
    
    login = UserLogin(
        email=mock_UserModel.email,
        password=mock_UserModel.password
    )
    
    repository = UserRepository()
    
    repository.create(data)
    
    # Act
    
    user = repository.get(login)
    
    # Assert
    
    assert isinstance(user, UserResponse)
    assert user.id == data.id
    assert user.username == data.username
    assert user.email == data.email
    assert user.created_at == data.created_at
    assert user.updated_at == data.updated_at

    
    
    result = repository.delete(
        UserLogin(
            email=mock_UserModel.email,
            password=mock_UserModel.password
        )
    )
    
    assert result is True
    
    
def test_UserRepository_get_fail_invalid_input(mock_UserModel):
    
    # Arrange
    data = mock_UserModel
    repository = UserRepository()
    
    # Act
    
    with raises(ValueError) as exc:
        repository.get(data)
    
    # Assert
    
    assert str(exc.value) == ERROR_USER_REPOSITORY_GET_INPUT_TYPE
    
    
def test_UserRepository_get_fail_invalid_password(mock_UserModel):
    
    # Arrange
    data = UserModel(**mock_UserModel.to_dict()) 
    
    login = UserLogin(
        email=mock_UserModel.email,
        password="wrong_passwordA123"
    )
    
    repository = UserRepository()
    
    repository.create(data)
    
    # Act
    
    user = repository.get(login)
    
    # Assert
    
    assert user is None
    
    
    result = repository.delete(
        UserLogin(
            email=mock_UserModel.email,
            password=mock_UserModel.password
        )
    )
    
    assert result is True
    
