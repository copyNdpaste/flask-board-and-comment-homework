import inject

from core.dto.comment_dto import CreateCommentDto
from core.repository.repository import Repository
from core.usecase_output import UseCaseSuccessOutput, UseCaseFailureOutput, FailureType


class CreateCommentUseCase:
    @inject.autoparams()
    def __init__(self, repo: Repository):
        self.repo = repo

    def execute(self, dto: CreateCommentDto):
        if (
            not dto.writer
            or not dto.contents
            or not dto.board_id
        ):
            return UseCaseFailureOutput(
                FailureType.INVALID_REQUEST_ERROR, "please check input values"
            )

        is_created = self.repo.create_comment(
            dto.board_id, dto.writer, dto.contents, dto.parent_id
        )
        if not is_created:
            return UseCaseFailureOutput(FailureType.INTERNAL_ERROR, "create comment fail")

        return UseCaseSuccessOutput(value=True)
