import inject

from core.dto.board_dto import CreateBoardDto
from core.repository.repository import Repository
from core.usecase_output import UseCaseSuccessOutput, UseCaseFailureOutput, FailureType


class CreateBoardUseCase:
    @inject.autoparams()
    def __init__(self, repo: Repository):
        self.repo = repo

    def execute(self, dto: CreateBoardDto):
        if (
            dto.title == None
            or dto.writer == None
            or dto.contents == None
            or dto.password == None
        ):
            return UseCaseFailureOutput(
                FailureType.INVALID_REQUEST_ERROR, "please check input values"
            )

        self.repo.create_board(dto.title, dto.writer, dto.contents, dto.password)

        return UseCaseSuccessOutput(value=True)
