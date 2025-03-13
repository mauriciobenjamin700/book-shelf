from src.backend.schemas.settings.base import BaseSchema
from src.backend.schemas.settings.fields import (
    id_field,
    username_field,
    email_field,
    password_field,
    created_at_field
)
from src.backend.schemas.settings.validators import(
    validate_username,
    validate_email,
    validate_password
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