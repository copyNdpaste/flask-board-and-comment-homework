from flask import request

from app.http.requests.board_request import CreateBoardRequest
from app.http.responses import failure_response
from app.http.responses.presenters.board_presenter import (
    CreateBoardPresenter,
)
from app.http.view import api

from core.usecases.create_board_usecase import CreateBoardUseCase
from core.usecase_output import UseCaseFailureOutput, FailureType


@api.route("/board", methods=["POST"])
def create_board_view():
    dto = CreateBoardRequest(**request.get_json()).validate_request_and_make_dto()
    if not dto:
        return failure_response(
            UseCaseFailureOutput(type=FailureType.INVALID_REQUEST_ERROR)
        )

    return CreateBoardPresenter().transform(CreateBoardUseCase().execute(dto=dto))
