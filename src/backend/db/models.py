from src.backend.schemas.settings.base import BaseSchema
from src.backend.schemas.settings.fields import (
    id_field,
    str_field,
    username_field,
    email_field,
    password_field,
    created_at_field,
    value_field
)
from src.backend.schemas.settings.validators import(
    validate_author,
    validate_pages,
    validate_title,
    validate_username,
    validate_email,
    validate_password,
    validate_year
)


class UserModel(BaseSchema):
    """
    User in DB schema

    - Args:
        - id: str
        - username: str
        - email: str
        - password: str
        - created_at: str
        - updated_at: str
    """
    id: str = id_field(generate=True)
    username: str = username_field()
    email: str = email_field()
    password: str = password_field()
    created_at: str = created_at_field(generate=True)
    updated_at: str = created_at_field(generate=True)

    _username_validator = validate_username
    _email_validator = validate_email
    _password_validator = validate_password
    

class BookModel(BaseSchema):
    """
    Book in DB schema
    
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
    id: str = id_field(generate=True)
    title: str = str_field("Título", "Título do Livro", "Livro de Python")
    author: str = str_field("Autor", "Autor do Livro", "José da Silva")
    pages: int = value_field("Páginas", "Número de Páginas", 100)
    year: int = value_field("Ano", "Ano de Publicação", 2021)
    created_at: str = created_at_field(generate=True)
    updated_at: str = created_at_field(generate=True,description="Data de Atualização")
    
    _title_validator = validate_title
    _author_validator = validate_author
    _pages_validator = validate_pages
    _year_validator = validate_year
    