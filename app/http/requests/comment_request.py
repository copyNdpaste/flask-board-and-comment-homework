from typing import Optional

from pydantic import ValidationError
from pydantic import BaseModel

from app.extensions.utils.log_helper import logger_

from core.dto.comment_dto import CreateCommentDto, GetCommentsDto

logger = logger_.getLogger(__name__)


class CreateCommentSchema(BaseModel):
    contents: str = None
    writer: str = None
    board_id: int = None
    parent_id: Optional[str] = None


class CreateCommentRequest:
    def __init__(self, contents, writer, board_id, parent_id=None):
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
                parent_id=self.parent_id,
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
            parent_id=self.parent_id,
        )


class GetCommentsSchema(BaseModel):
    id: Optional[int] = None
    board_id: int = None


class GetCommentsRequest:
    def __init__(
        self,
        id,
        board_id,
    ):
        self.id = id
        self.board_id = board_id

    def validate_request_and_make_dto(self):
        try:
            GetCommentsSchema(
                id=self.id,
                board_id=self.board_id,
            )
            return self.to_dto()
        except ValidationError as e:
            logger.error(
                f"[GetCommentsRequest][validate_request_and_make_dto] error : {e}"
            )
            return False

    def to_dto(self) -> GetCommentsDto:
        return GetCommentsDto(
            id=self.id,
            board_id=self.board_id,
        )
