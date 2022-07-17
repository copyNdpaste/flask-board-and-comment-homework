import inject

from app.extensions.utils.notification_helper import notify_keyword_contents
from core.dto.board_dto import CreateBoardDto
from core.repository.repository import Repository
from core.usecase_output import UseCaseSuccessOutput, UseCaseFailureOutput, FailureType


class CreateBoardUseCase:
    @inject.autoparams()
    def __init__(self, repo: Repository):
        self.repo = repo

    def execute(self, dto: CreateBoardDto):
        if not dto.title or not dto.writer or not dto.contents or not dto.password:
            return UseCaseFailureOutput(
                FailureType.INVALID_REQUEST_ERROR, "please check input values"
            )

        board = self.repo.create_board(
            dto.title, dto.writer, dto.contents, dto.password
        )
        if not board:
            return UseCaseFailureOutput(FailureType.INTERNAL_ERROR, "create board fail")

        notify_keyword_contents("board", board.contents, board.id)

        return UseCaseSuccessOutput(value=True)
