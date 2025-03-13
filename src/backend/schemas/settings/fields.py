from pydantic import Field

from src.backend.utils.generate import id_generate, get_current_date

def base_field(title: str, description: str, example: str) -> Field:
    
    return Field(
        None,
        title=title,
        description=description,
        examples=[example],
        validate_default=True
    )

def created_at_field(
        title: str = "Data", 
        description:str = "Data de Criação", 
        example: str = "2025-12-25", 
        generate: bool = False
    ) -> Field:

    if generate:
        return Field(
            default_factory=get_current_date,
            frozen=True,
            title=title,
            description=description,
            example=[example],
            validate_default=True
        )
    
    return base_field(title, description, example)


def email_field(title: str = "E-mail", description: str = "E-mail", example: str = "email@gmail.com") -> Field:
    
    return base_field(title, description, example)

def id_field(title: str = "ID", description: str = "ID", example: str = "1234567890", generate: bool = False) -> Field:
    
    if generate:
        return Field(
            default_factory=id_generate,
            frozen=True,
            title=title,
            description=description,
            example=example
        )
    return base_field(title, description, example)

def message_field(title: str = "Mensagem", description: str = "Mensagem", example: str = "Mensagem") -> Field:
    
    return base_field(title, description, example)

def username_field(title: str = "Nome", description: str = "Nome", example: str = "Jose") -> Field:
    
    return base_field(title, description, example)

def password_field(title: str = "Senha", description: str = "Senha", example: str = "password1234") -> Field:
    
    return base_field(title, description, example)

def phone_field(title: str = "Telefone", description: str = "Telefone", example: str = "(11) 99999-9999") -> Field:
    
    return base_field(title, description, example)

def value_field(title: str = "Valor", description: str = "Valor", example: float = 100.00) -> Field:
    
    return base_field(title, description, example)

    