import inject

from app.extensions.utils.notification_helper import notify_keyword_contents
from core.dto.comment_dto import CreateCommentDto
from core.repository.repository import Repository
from core.usecase_output import UseCaseSuccessOutput, UseCaseFailureOutput, FailureType


class CreateCommentUseCase:
    @inject.autoparams()
    def __init__(self, repo: Repository):
        self.repo = repo

    def execute(self, dto: CreateCommentDto):
        if not dto.writer or not dto.contents or not dto.board_id:
            return UseCaseFailureOutput(
                FailureType.INVALID_REQUEST_ERROR, "please check input values"
            )

        comment = self.repo.create_comment(
            dto.board_id, dto.writer, dto.contents, dto.parent_id
        )
        if not comment:
            return UseCaseFailureOutput(
                FailureType.INTERNAL_ERROR, "create comment fail"
            )

        notify_keyword_contents(
            "comment", comment.contents, comment.board_id, comment.id
        )

        return UseCaseSuccessOutput(value=True)
