from typing import Optional

from pydantic import ValidationError
from pydantic import BaseModel

from app.extensions.utils.log_helper import logger_

from core.dto.board_dto import (
    CreateBoardDto,
    UpdateBoardDto,
    DeleteBoardDto,
    GetBoardsDto,
)
from core.dto.comment_dto import CreateCommentDto

logger = logger_.getLogger(__name__)


class CreateCommentSchema(BaseModel):
    contents: str = None
    writer: str = None
    board_id:int=None
    parent_id:Optional[str]=None


class CreateCommentRequest:
    def __init__(self, contents, writer, board_id,parent_id=None):
        self.contents = contents
        self.writer = writer
        self.board_id = board_id
        self.parent_id = parent_id

    def validate_request_and_make_dto(self):
        try:
            CreateCommentSchema(
                contents=self.contents,
                writer=self.writer,
                 board_id=self.board_id,
             parent_id=self.parent_id
            )
            return self.to_dto()
        except ValidationError as e:
            logger.error(
                f"[CreateCommentRequest][validate_request_and_make_dto] error : {e}"
            )
            return False

    def to_dto(self) -> CreateCommentDto:
        return CreateCommentDto(
            contents=self.contents,
            writer=self.writer,
            board_id=self.board_id,
            parent_id=self.parent_id
        )


class GetBoardsSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    writer: Optional[str] = None


class GetBoardsRequest:
    def __init__(self, id, title, writer):
        self.id = id
        self.title = title
        self.writer = writer

    def validate_request_and_make_dto(self):
        try:
            GetBoardsSchema(
                id=self.id,
                title=self.title,
                writer=self.writer,
            )
            return self.to_dto()
        except ValidationError as e:
            logger.error(
                f"[GetBoardsRequest][validate_request_and_make_dto] error : {e}"
            )
            return False

    def to_dto(self) -> GetBoardsDto:
        return GetBoardsDto(
            id=self.id,
            title=self.title,
            writer=self.writer,
        )

