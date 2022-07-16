from pydantic import ValidationError
from pydantic import BaseModel

from app.extensions.utils.log_helper import logger_

from core.dto.board_dto import CreateBoardDto, UpdateBoardDto, DeleteBoardDto

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
