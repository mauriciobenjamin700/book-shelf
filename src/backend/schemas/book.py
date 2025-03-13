from src.backend.schemas.settings.base import BaseSchema
from src.backend.schemas.settings.fields import (
    created_at_field,
    str_field,
    value_field
)
from src.backend.schemas.settings.validators import (
    validate_author,
    validate_pages,
    validate_title,
    validate_year
)


class BookRequest(BaseSchema):
    """
    Schema with the fields to create a new Book
    
    - Args:
        - title: str
        - author: str
        - pages: int
        - year: int
    
    - Attributes:
        - title: str
        - author: str
        - pages: int
        - year: int
    """
    title: str = str_field("Título", "Título do Livro", "Livro de Python")
    author: str = str_field("Autor", "Autor do Livro", "José da Silva")
    pages: int = value_field("Páginas", "Número de Páginas", 100)
    year: int = value_field("Ano", "Ano de Publicação", 2021)
    
    _title_validator = validate_title
    _author_validator = validate_author
    _pages_validator = validate_pages
    _year_validator = validate_year
    
    
class BookResponse(BaseSchema):
    """
    Schema with the fields to return a Book
    
    - Args:
        - id: str
        - title: str
        - author: str
        - pages: int
        - year: int
        - created_at: str
        - updated_at: str
        
    - Attributes:
        - id: str
        - title: str
        - author: str
        - pages: int
        - year: int
        - created_at: str
        - updated_at: str
    """
    id: str = str_field("ID", "ID do Livro", "1")
    title: str = str_field("Título", "Título do Livro", "Livro de Python")
    author: str = str_field("Autor", "Autor do Livro", "José da Silva")
    pages: int = value_field("Páginas", "Número de Páginas", 100)
    year: int = value_field("Ano", "Ano de Publicação", 2021)
    created_at: str = created_at_field()
    updated_at: str = created_at_field(description="Data de Atualização")
    
    _title_validator = validate_title
    _author_validator = validate_author
    _pages_validator = validate_pages
    _year_validator = validate_year
    

class BookFilters(BaseSchema):
    """
    Schema with the fields to filter Books
    
    - Args:
        - title: str | None
        - author: str | None
        - pages: int | None
        - year: int | None
    - Attributes:
        - title: str | None
        - author: str | None
        - pages: int | None
        - year: int | None
    """
    title: str | None = str_field("Título", "Título do Livro", "Livro de Python")
    author: str | None = str_field("Autor", "Autor do Livro", "José da Silva")
    pages: int | None = value_field("Páginas", "Número de Páginas", 100)
    year: int | None = value_field("Ano", "Ano de Publicação", 2021)