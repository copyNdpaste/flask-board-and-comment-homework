import inject

from core.dto.board_dto import DeleteBoardDto
from core.repository.repository import Repository
from core.usecase_output import UseCaseSuccessOutput, UseCaseFailureOutput, FailureType


class DeleteBoardUseCase:
    @inject.autoparams()
    def __init__(self, repo: Repository):
        self.repo = repo

    def execute(self, dto: DeleteBoardDto):
        board = self.repo.get_board(id=dto.id)
        if not board:
            return UseCaseFailureOutput(FailureType.NOT_FOUND_ERROR, "board not found")
        if board.password != dto.password:
            return UseCaseFailureOutput(
                FailureType.UNAUTHORIZED_ERROR, "please check password"
            )

        is_deleted = self.repo.delete_board(dto.id)

        if not is_deleted:
            return UseCaseFailureOutput(FailureType.INTERNAL_ERROR, "delete board fail")

        return UseCaseSuccessOutput(value=True)
