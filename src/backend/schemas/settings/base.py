from pydantic import BaseModel


class BaseSchema(BaseModel):
    """
    Base schema class that extends the pydantic BaseModel.

    - Methods:
        - to_dict: Method that returns the data of the schema as a dictionary, excluding fields and including fields if specified.
    """
    
    def to_dict(
        self,
        exclude_fields: list[str] = [],
        include_fields: dict = {},
        exclude_none: bool = False,
    ) -> dict:
        """
        Converts the schema to a dictionary.

        - Args:
            - exclude_fields: list[str]: A list of field usernames to exclude from the resulting dictionary.
            - include_fields: dict: A dictionary of field usernames and their values to include in the resulting dictionary.
            - exclude_none: bool: A flag indicating whether to exclude fields with a value of None from the resulting dictionary.

        - Returns:
            - dict: The data of the schema as a dictionary.
        """
        
        data = self.model_dump()
        
        data = {k: v for k, v in data.items() if k not in exclude_fields and (not exclude_none or v is not None)}
        
        data.update(include_fields)
        
        return data
        

class ValidationError(Exception):
    """
    A class that represents the validation error on a schema.
    
    - Args:
        - field: str: The field that has the error.
        - detail: str: The error message.
    """
    def __init__(self, field: str, detail: str):
    
        self.field = field
        self.detail = detail
        super().__init__(f"{field}: {detail}")
        
        
class RequestError(Exception):
    """
    A class that represents the request error on a schema.
    
    - Args:
        - status: int: The status code of the error.
        - detail: str: The error message.
        
    - Status Legend:
        - 401 - Unauthorized
        - 404 - Not Found
        - 409 - Conflict
        - 500 - Internal Server Error
    """
    def __init__(self, status: int, detail: str):
        
        self.status_code = status
        self.detail = detail
        super().__init__(detail)