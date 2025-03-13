from pytest import raises

from src.backend.constants.messages.server import *
from src.backend.db.models import UserModel
from src.backend.db.repositories.user import UserRepository
from src.backend.schemas.user import (
    UserLogin,
    UserResponse
)


def test_UserRepository_delete_success(mock_UserModel):
    
    # Arrange
    data = UserModel(**mock_UserModel.to_dict()) 
    
    login = UserLogin(
        email=mock_UserModel.email,
        password=mock_UserModel.password
    )
    
    repository = UserRepository()
    
    repository.create(data)
    
    # Act
    
    result = repository.delete(login)
    
    # Assert
    
    assert isinstance(result, bool)
    assert result is True

    user = repository.get(login)
    
    assert user is None
    
    
def test_UserRepository_delete_fail_invalid_input(mock_UserModel):
    
    # Arrange
    data = mock_UserModel
    repository = UserRepository()
    
    # Act
    
    with raises(ValueError) as exc:
        repository.delete(data)
    
    # Assert
    
    assert str(exc.value) == ERROR_USER_REPOSITORY_GET_INPUT_TYPE
    
    
def test_UserRepository_delete_fail_user_not_found(mock_UserModel):
    
    # Arrange
    data = UserModel(**mock_UserModel.to_dict()) 
    
    login = UserLogin(
        email="wrong@gmail.com",
        password="wrong_passwordA123"
    )
    
    repository = UserRepository()
    
    # Act
    
    result = repository.delete(login)
    
    # Assert
    
    assert result is False
    
    
