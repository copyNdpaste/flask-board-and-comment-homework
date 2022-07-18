from datetime import datetime
from pydantic import BaseModel


class BoardEntity(BaseModel):
    id: int = None
    title: str = None
    contents: str = None
    writer: str = None
    password: str = None
    created_at: datetime = None
    updated_at: datetime = None
