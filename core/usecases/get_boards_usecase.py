import inject

from core.dto.board_dto import GetBoardsDto
from core.repository.repository import Repository
from core.usecase_output import UseCaseSuccessOutput, UseCaseFailureOutput, FailureType


class GetBoardsUseCase:
    @inject.autoparams()
    def __init__(self, repo: Repository):
        self.repo = repo

    def execute(self, dto: GetBoardsDto):
        boards = self.repo.get_boards(dto.id, dto.writer, dto.title)

        if boards is False:
            return UseCaseFailureOutput(FailureType.INTERNAL_ERROR, "get boards fail")

        return UseCaseSuccessOutput(
            value=boards, meta=boards[-1].id - 1 if boards else None
        )
