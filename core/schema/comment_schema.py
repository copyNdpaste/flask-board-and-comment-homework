from datetime import datetime
from typing import List

from pydantic import BaseModel


class GetCommentResponseSchema(BaseModel):
    id: int = None
    contents: str = None
    writer: str = None
    created_at: datetime = None
    child: List = []


class GetCommentsResponseSchema(BaseModel):
    comments: List[GetCommentResponseSchema]
