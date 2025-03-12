from src.backend.schemas.settings.base import BaseSchema
from src.backend.schemas.settings.fields import(
    created_at_field,
    email_field,
    id_field,
    name_field,
    password_field
)
from src.backend.schemas.settings.validators import(
    validate_email,
    validate_name,
    validate_password
)

class UserLogin(BaseSchema):
    """
    User login schema.

    - Args:
        - email: str
        - password: str

    - Attributes:
        - email: str
        - password: str
    """
    email: str = email_field()
    password: str = password_field()

    _email_validator = validate_email
    _password_validator = validate_password


class UserRegister(BaseSchema):
    """
    User registration schema.

    - Args:
        - name: str
        - email: str
        - password: str

    - Attributes:
        - name: str
        - email: str
        - password: str
    """
    name: str = name_field()
    email: str = email_field()
    password: str = password_field()
    
    _name_validator = validate_name
    _email_validator = validate_email
    _password_validator = validate_password


class UserDB(BaseSchema):
    """
    User in DB schema

    - Args:
        - id: str
        - name: str
        - email: str
        - password: str
        - created_at: str
        - updated_at: str
    """
    id: str = id_field(generate=True)
    name: str = name_field()
    email: str = email_field()
    password: str = password_field()
    created_at: str = created_at_field(generate=True)
    updated_at: str = created_at_field(generate=True)

    _name_validator = validate_name
    _email_validator = validate_email
    _password_validator = validate_password


class UserResponse(BaseSchema):
    """
    Data with user information

    - Args:
        - id: str
        - name: str
        - email: str
        - created_at: str
        - updated_at: str
    """
    id: str = id_field()
    name: str = name_field()
    email: str = email_field()
    created_at: str = created_at_field(generate=False)
    updated_at: str = created_at_field(generate=False)
    
    _name_validator = validate_name
    _email_validator = validate_email