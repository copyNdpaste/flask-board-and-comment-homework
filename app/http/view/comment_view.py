from flask import request

from app.http.requests.comment_request import CreateCommentRequest
from app.http.responses import failure_response

from app.http.responses.presenters.comment_presenter import CreateCommentPresenter
from app.http.view import api

from core.usecase_output import UseCaseFailureOutput, FailureType
from core.usecases.create_comment_usecase import CreateCommentUseCase


@api.route("/comment", methods=["POST"])
def create_comment_view():
    dto = CreateCommentRequest(**request.get_json()).validate_request_and_make_dto()
    if not dto:
        return failure_response(
            UseCaseFailureOutput(type=FailureType.INVALID_REQUEST_ERROR)
        )

    return CreateCommentPresenter().transform(CreateCommentUseCase().execute(dto=dto))
