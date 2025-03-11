# Database Entities

## User

- id: str
- name: str
- email: str
- password: str
- created_at: datetime
- updated_at: datetime

## Book

- id: str
- name: str
- author: str
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
