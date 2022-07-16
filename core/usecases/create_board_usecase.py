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

        is_created = self.repo.create_board(dto.title, dto.writer, dto.contents, dto.password)
        if not is_created:
            return UseCaseFailureOutput(FailureType.INTERNAL_ERROR, "create board fail")

        return UseCaseSuccessOutput(value=True)
