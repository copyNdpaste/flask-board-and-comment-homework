from flask import request

from app.http.requests.comment_request import CreateCommentRequest, GetCommentsRequest
from app.http.responses import failure_response

from app.http.responses.presenters.comment_presenter import (
    CreateCommentPresenter,
    GetCommentsPresenter,
)
from app.http.view import api

from core.usecase_output import UseCaseFailureOutput, FailureType
from core.usecases.create_comment_usecase import CreateCommentUseCase
from core.usecases.get_comments_usecase import GetCommentsUseCase


@api.route("/comment", methods=["POST"])
def create_comment_view():
    dto = CreateCommentRequest(**request.get_json()).validate_request_and_make_dto()
    if not dto:
        return failure_response(
            UseCaseFailureOutput(type=FailureType.INVALID_REQUEST_ERROR)
        )

    return CreateCommentPresenter().transform(CreateCommentUseCase().execute(dto=dto))


@api.route("/comments", methods=["GET"])
def get_comments_view():
    dto = GetCommentsRequest(**request.get_json()).validate_request_and_make_dto()
    if not dto:
        return failure_response(
            UseCaseFailureOutput(type=FailureType.INVALID_REQUEST_ERROR)
        )

    return GetCommentsPresenter().transform(GetCommentsUseCase().execute(dto=dto))
