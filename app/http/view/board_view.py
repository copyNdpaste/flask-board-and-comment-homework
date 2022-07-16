from flask import request

from app.http.requests.board_request import (
    CreateBoardRequest,
    UpdateBoardRequest,
    DeleteBoardRequest,
)
from app.http.responses import failure_response
from app.http.responses.presenters.board_presenter import (
    CreateBoardPresenter,
    UpdateBoardPresenter,
    DeleteBoardPresenter,
)
from app.http.view import api

from core.usecases.create_board_usecase import CreateBoardUseCase
from core.usecase_output import UseCaseFailureOutput, FailureType
from core.usecases.delete_board_usecase import DeleteBoardUseCase
from core.usecases.update_board_usecase import UpdateBoardUseCase


@api.route("/board", methods=["POST"])
def create_board_view():
    dto = CreateBoardRequest(**request.get_json()).validate_request_and_make_dto()
    if not dto:
        return failure_response(
            UseCaseFailureOutput(type=FailureType.INVALID_REQUEST_ERROR)
        )

    return CreateBoardPresenter().transform(CreateBoardUseCase().execute(dto=dto))


@api.route("/board", methods=["PUT"])
def update_board_view():
    dto = UpdateBoardRequest(**request.get_json()).validate_request_and_make_dto()
    if not dto:
        return failure_response(
            UseCaseFailureOutput(type=FailureType.INVALID_REQUEST_ERROR)
        )

    return UpdateBoardPresenter().transform(UpdateBoardUseCase().execute(dto=dto))


@api.route("/board", methods=["DELETE"])
def delete_board_view():
    dto = DeleteBoardRequest(**request.get_json()).validate_request_and_make_dto()
    if not dto:
        return failure_response(
            UseCaseFailureOutput(type=FailureType.INVALID_REQUEST_ERROR)
        )

    return DeleteBoardPresenter().transform(DeleteBoardUseCase().execute(dto=dto))
