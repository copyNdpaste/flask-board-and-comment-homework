from datetime import datetime
from typing import List

from pydantic import BaseModel


class GetBoardResponseSchema(BaseModel):
    id: int = None
    title: str = None
    contents: str = None
    writer: str = None
    password: str = None
    created_at: datetime = None
    updated_at: datetime = None


class GetBoardsResponseSchema(BaseModel):
    boards: List[GetBoardResponseSchema]
