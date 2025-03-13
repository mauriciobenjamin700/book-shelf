from src.backend.db.models import BookModel
from src.backend.db.repositories.book import BookRepository
from src.backend.schemas.book import BookRequest


def test_BookRepository_update_success(mock_BookModel):
    
    # Arrange
    data  = BookModel(**mock_BookModel.to_dict())
    repository = BookRepository()
    book = repository.create(data)
    
    new = BookRequest(
        title = "New Title",
        author = "New Author",
        pages = 100,
        year = 2025
    )
    
    # Act
    
    response = repository.update(book.id, new)

    
    # Assert

    assert response is not None
    assert response.id == mock_BookModel.id
    assert response.title == new.title
    assert response.author == new.author
    assert response.pages == new.pages
    assert response.year == new.year
    
    result = repository.delete(response.id)
    
    assert result == True