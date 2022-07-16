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
