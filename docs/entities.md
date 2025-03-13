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
- title: str
- author: str
- pages: int
- year: int
- created_at: str
- updated_at: str

## Favorite

- id: str
- book_id: str
- user_id: str
- created_at: datetime
- updated_at: datetime
