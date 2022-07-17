from core.dto.board_dto import CreateBoardDto
from core.usecase_output import FailureType
from core.usecases.create_board_usecase import CreateBoardUseCase


def test_create_board_then_success(session):
    title = "test_title"
    contents = "test_contents"
    writer = "test_writer"
    password = "test_password"

    dto = CreateBoardDto(
        title=title, contents=contents, writer=writer, password=password
    )

    usecase = CreateBoardUseCase()

    assert usecase.execute(dto=dto).value


def test_when_create_board_with_wrong_params_then_fail(session):
    title = "test_title"
    contents = "test_contents"
    writer = "test_writer"

    dto = CreateBoardDto(
        title=title,
        contents=contents,
        writer=writer,
    )

    usecase = CreateBoardUseCase()

    assert usecase.execute(dto=dto).type == FailureType.INVALID_REQUEST_ERROR


def test_create_board_contain_keyword_then_success(session, create_keywords):
    title = "test_title"
    contents = "1"
    writer = "test_writer"
    password = "test_password"

    create_keywords(1, "writer 1")
    create_keywords(2, "writer 2")

    dto = CreateBoardDto(
        title=title, contents=contents, writer=writer, password=password
    )

    usecase = CreateBoardUseCase()

    assert usecase.execute(dto=dto).value
