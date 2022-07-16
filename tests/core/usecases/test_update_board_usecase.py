from core.dto.board_dto import UpdateBoardDto
from core.repository.repository import Repository
from core.usecase_output import FailureType
from core.usecases.update_board_usecase import UpdateBoardUseCase


def test_update_board_then_success(session):
    title = "test_title"
    contents = "test_contents"
    writer = "test_writer"
    password = "test_password"
    Repository().create_board(
        title=title, writer=writer, contents=contents, password=password
    )

    id = 1
    title = "test_title_2"
    contents = "test_contents_2"
    password = "test_password"

    dto = UpdateBoardDto(
       id = id, title=title, contents=contents, password=password
    )

    usecase = UpdateBoardUseCase()

    assert usecase.execute(dto=dto).value


def test_when_update_board_with_wrong_params_then_fail(session):
    title = "test_title"
    contents = "test_contents"
    writer = "test_writer"
    password = "test_password"
    Repository().create_board(
        title=title, writer=writer, contents=contents, password=password
    )

    id = 1
    password = "test_password"

    dto = UpdateBoardDto(
        id=id, password=password
    )

    usecase = UpdateBoardUseCase()

    assert usecase.execute(dto=dto).type == FailureType.INVALID_REQUEST_ERROR


def test_when_update_board_with_wrong_password_then_fail(session):
    title = "test_title"
    contents = "test_contents"
    writer = "test_writer"
    password = "test_password"
    Repository().create_board(
        title=title, writer=writer, contents=contents, password=password
    )

    id = 1
    title = "test_title_2"
    contents = "test_contents_2"
    password = "1"

    dto = UpdateBoardDto(
        id=id, title=title, contents=contents, password=password
    )

    usecase = UpdateBoardUseCase()

    assert usecase.execute(dto=dto).type == FailureType.UNAUTHORIZED_ERROR
