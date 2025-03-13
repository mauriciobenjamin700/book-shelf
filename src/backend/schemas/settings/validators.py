from pydantic import field_validator
from re import match

from src.backend.constants.messages.book import *
from src.backend.constants.messages.user import *
from src.backend.schemas.settings.base import ValidationError


@field_validator("email", mode="before")
def validate_email(cls, value: str) -> str:
    """
    A function that validates the email field.

    - Args:
        - cls: The class instance.
        - value: The email value.
    - Returns:
        - str: The email value.
    """

    if not value:

        raise ValidationError(
            field="email",
            detail=ERROR_USER_REQUIRED_FIELD_EMAIL
        )

    if not isinstance(value, str):
        raise ValidationError(field="email", detail=ERROR_EMAIL_INVALID_FORMAT_TYPE)
    
    value = value.strip()
    
    if not match(r"[^@]+@[^@]+\.[^@]+", value):
        raise ValidationError(field="email", detail=ERROR_EMAIL_INVALID_FORMAT_MASK)
    
    return value

@field_validator("is_admin", mode="before")
def validate_is_admin(cls, value: bool) -> bool:
    """
    A function that validates the is_admin field.

    - Args:
        - cls: The class instance.
        - value: The is_admin value.
    - Returns:
        - bool: The is_admin value.
    """
    if not isinstance(value, bool):
        raise ValidationError(field="is_admin", detail=ERROR_IS_ADMIN_INVALID_FORMAT_TYPE)
    return value

@field_validator("username", mode="before")
def validate_username(cls, value: str) -> str:
    """
    A function that validates the username field.

    - Args:
        - cls: The class instance.
        - value: The username value.
    - Returns:
        - str: The username value.
    """
    if not value:
        raise ValidationError(
            "username",
            ERROR_USER_REQUIRED_FIELD_USERNAME
        )

    if not isinstance(value, str):
        raise ValidationError(field="username", detail=ERROR_USERNAME_INVALID_FORMAT_TYPE)
    
    value = value.strip()
    
    if len(value) <= 1:
        raise ValidationError(field="username", detail=ERROR_USERNAME_INVALID_FORMAT_MIN_LENGTH)
    
    value = value.upper()
    
    return value

@field_validator("password", mode="before")
def validate_password(cls, value: str) -> str:
    """
    A function that validates the password field.

    - Args:
        - cls: The class instance.
        - value: The password value.
    - Returns:
        - str: The password value.
    """
    if not value:
        raise ValidationError(
            "password",
            ERROR_USER_REQUIRED_FIELD_PASSWORD
        )

    if not isinstance(value, str):
        raise ValidationError(field="password", detail=ERROR_PASSWORD_INVALID_FORMAT_TYPE)
    
    value = value.strip()
    
    if len(value) < 8:
        raise ValidationError(field="password", detail=ERROR_PASSWORD_INVALID_FORMAT_MIN_LENGTH)
    
    if len(value) > 255:
        raise ValidationError(field="password", detail=ERROR_PASSWORD_INVALID_FORMAT_MAX_LENGTH)
    
    if not any(char.isdigit() for char in value):
        raise ValidationError(field="password", detail=ERROR_PASSWORD_INVALID_FORMAT_DIGIT)
    
    if not any(char.islower() for char in value):
        raise ValidationError(field="password", detail=ERROR_PASSWORD_INVALID_FORMAT_LOWERCASE)
    
    if not any(char.isupper() for char in value):
        raise ValidationError(field="password", detail=ERROR_PASSWORD_INVALID_FORMAT_UPPERCASE)
    
    if not any(char in "!@#$%&*()_+-=[]{};:,.<>?/" for char in value):
        raise ValidationError(field="password", detail=ERROR_PASSWORD_INVALID_FORMAT_SPECIAL_CHARACTER)
    
    return value

@field_validator("title", mode="before")
def validate_title(cls, value: str) -> str:
    """
    A function that validates the title field.

    - Args:
        - cls: The class instance.
        - value: The title value.
    - Returns:
        - str: The title value.
    """
    if not value:
        raise ValidationError(
            "title",
            ERROR_USER_REQUIRED_FIELD_TITLE
        )

    if not isinstance(value, str):
        raise ValidationError(field="title", detail=ERROR_TITLE_INVALID_FORMAT_TYPE)
    
    value = value.strip()
    value = value.upper()
    
    if len(value) <= 1:
        raise ValidationError(field="title", detail=ERROR_TITLE_INVALID_FORMAT_MIN_LENGTH)
    
    if len(value) > 255:
        raise ValidationError(field="title", detail=ERROR_TITLE_INVALID_FORMAT_MAX_LENGTH)
    
    
    return value

@field_validator("author", mode="before")
def validate_author(cls, value: str) -> str:
    """
    A function that validates the author field.
    
    - Args:
        - cls: The class instance.
        - value: The username value.
    - Returns:
        - str: The username value.
    """
    if not value:
        raise ValidationError(
            "author",
            ERROR_AUTHOR_REQUIRED_FIELD_AUTHOR
        )

    if not isinstance(value, str):
        raise ValidationError(field="title", detail=ERROR_AUTHOR_INVALID_FORMAT_TYPE)
    
    value = value.strip()
    value = value.upper()
    
    if len(value) <= 1:
        raise ValidationError(field="title", detail=ERROR_AUTHOR_INVALID_FORMAT_MIN_LENGTH)
    
    if len(value) > 255:
        raise ValidationError(field="title", detail=ERROR_AUTHOR_INVALID_FORMAT_MAX_LENGTH)
    
    
    return value


@field_validator("pages", mode="before")
def validate_pages(cls, value: int):
    
    if not isinstance(value, int):
        raise ValidationError(field="pages", detail=ERROR_PAGES_INVALID_FORMAT_TYPE)
    
    if value <= 0:
        raise ValidationError(field="pages", detail=ERROR_PAGES_INVALID_FORMAT_MIN_VALUE)
    
    return value


@field_validator("year", mode="before")
def validate_year(cls, value: int):
    
    if not isinstance(value, int):
        raise ValidationError(field="year", detail=ERROR_YEAR_INVALID_FORMAT_TYPE)
    
    if value <= 0:
        raise ValidationError(field="year", detail=ERROR_YEAR_INVALID_FORMAT_MIN_VALUE)
    
    
    return value