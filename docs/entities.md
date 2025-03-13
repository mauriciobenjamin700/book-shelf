# Database Entities

## User

- id: str
- username: str
- email: str
- password: str
- created_at: datetime
- updated_at: datetime

## Book

- id: str
- username: str
- author: str
- pages: int
- year: str
- gender: str
- description: str
- created_at: str
- updated_at: str

## Favorite

- id: str
- book_id: str
- user_id: str
- created_at: datetime
- updated_at: datetime
