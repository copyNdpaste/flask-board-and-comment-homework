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

logger = logger_.getLogger(__name__)


class CreateBoardSchema(BaseModel):
    title: str = None
    contents: str = None
    writer: str = None
    password: str = None


class CreateBoardRequest:
    def __init__(self, title, contents, writer, password):
        self.title = title
        self.contents = contents
        self.writer = writer
        self.password = password

    def validate_request_and_make_dto(self):
        try:
            CreateBoardSchema(
                title=self.title,
                contents=self.contents,
                writer=self.writer,
                password=self.password,
            )
            return self.to_dto()
        except ValidationError as e:
            logger.error(
                f"[CreateBoardRequest][validate_request_and_make_dto] error : {e}"
            )
            return False

    def to_dto(self) -> CreateBoardDto:
        return CreateBoardDto(
            title=self.title,
            contents=self.contents,
            writer=self.writer,
            password=self.password,
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


class UpdateBoardSchema(BaseModel):
    id: int = None
    title: str = None
    contents: str = None
    password: str = None


class UpdateBoardRequest:
    def __init__(self, id, title, contents, password):
        self.id = id
        self.title = title
        self.contents = contents
        self.password = password

    def validate_request_and_make_dto(self):
        try:
            UpdateBoardSchema(
                id=self.id,
                title=self.title,
                contents=self.contents,
                password=self.password,
            )
            return self.to_dto()
        except ValidationError as e:
            logger.error(
                f"[UpdateBoardRequest][validate_request_and_make_dto] error : {e}"
            )
            return False

    def to_dto(self) -> UpdateBoardDto:
        return UpdateBoardDto(
            id=self.id,
            title=self.title,
            contents=self.contents,
            password=self.password,
        )


class DeleteBoardSchema(BaseModel):
    id: int = None
    password: str = None


class DeleteBoardRequest:
    def __init__(self, password):
        self.id = id
        self.password = password

    def validate_request_and_make_dto(self):
        try:
            UpdateBoardSchema(
                id=self.id,
                password=self.password,
            )
            return self.to_dto()
        except ValidationError as e:
            logger.error(
                f"[DeleteBoardRequest][validate_request_and_make_dto] error : {e}"
            )
            return False

    def to_dto(self) -> DeleteBoardDto:
        return DeleteBoardDto(
            id=self.id,
            password=self.password,
        )
