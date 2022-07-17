from pydantic import BaseModel


class CreateCommentDto(BaseModel):
    contents: str = None
    writer: str = None
    board_id: int = None
    parent_id: int = None


class GetCommentsDto(BaseModel):
    board_id: int = None
