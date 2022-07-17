from datetime import datetime
from pydantic import BaseModel

from core.entity.board_entity import BoardEntity


class CommentEntity(BaseModel):
    id: int = None
    contents: str = None
    writer: str = None
    password: str = None
    parent_id: int = None
    board_id: int = None
    created_at: datetime = None
    child: list = []
