import inject

from core.dto.comment_dto import GetCommentsDto
from core.repository.repository import Repository
from core.usecase_output import UseCaseSuccessOutput, UseCaseFailureOutput, FailureType


class GetCommentsUseCase:
    @inject.autoparams()
    def __init__(self, repo: Repository):
        self.repo = repo

    def execute(self, dto: GetCommentsDto):
        comments = self.repo.get_comments(dto.id, dto.board_id)

        if not comments:
            return UseCaseFailureOutput(FailureType.INTERNAL_ERROR, "get comments fail")

        return UseCaseSuccessOutput(
            value=comments, meta=comments[-1].id + 1 if comments and len(comments) == 10 else None
        )
