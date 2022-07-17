import inject

from core.dto.board_dto import UpdateBoardDto
from core.repository.repository import Repository
from core.usecase_output import UseCaseSuccessOutput, UseCaseFailureOutput, FailureType


class UpdateBoardUseCase:
    @inject.autoparams()
    def __init__(self, repo: Repository):
        self.repo = repo

    def execute(self, dto: UpdateBoardDto):
        board = self.repo.get_board(id=dto.id)
        if board.password != dto.password:
            return UseCaseFailureOutput(
                FailureType.UNAUTHORIZED_ERROR, "please check password"
            )

        if dto.title == '' or dto.contents == '':
            return UseCaseFailureOutput(
                FailureType.INVALID_REQUEST_ERROR, "please check input values"
            )

        is_updated = self.repo.update_board(dto.id, dto.title, dto.contents)

        if not is_updated:
            return UseCaseFailureOutput(FailureType.INTERNAL_ERROR, "update board fail")

        return UseCaseSuccessOutput(value=True)
