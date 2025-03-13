from src.backend.db.models import BookModel
from src.backend.db.repositories.book import BookRepository


def test_BookRepository_get_all_success(mock_BookModel):
    
    # Arrange
    data  = BookModel(**mock_BookModel.to_dict())
    repository = BookRepository()
    repository.create(data)
    
    # Act
    
    responses = repository.get(None)

    
    # Assert
    assert len(responses) > 0
    response = responses[0]
    assert response is not None
    assert response.id == mock_BookModel.id
    assert response.title == mock_BookModel.title
    assert response.author == mock_BookModel.author
    assert response.pages == mock_BookModel.pages
    assert response.year == mock_BookModel.year
    assert response.created_at == mock_BookModel.created_at
    assert response.updated_at == mock_BookModel.updated_at
    
    result = repository.delete(response.id)
    
    assert result == True