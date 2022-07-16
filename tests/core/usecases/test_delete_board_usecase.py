from core.dto.board_dto import UpdateBoardDto, DeleteBoardDto
from core.repository.repository import Repository
from core.usecase_output import FailureType
from core.usecases.delete_board_usecase import DeleteBoardUseCase
from core.usecases.update_board_usecase import UpdateBoardUseCase


def test_delete_board_then_success(session):
    title = "test_title"
    contents = "test_contents"
    writer = "test_writer"
    password = "test_password"
    Repository().create_board(
        title=title, writer=writer, contents=contents, password=password
    )

    id = 1

    dto = DeleteBoardDto(id=id)

    usecase = DeleteBoardUseCase()

    assert usecase.execute(dto=dto).value


def test_when_delete_board_with_wrong_password_then_fail(session):
    title = "test_title"
    contents = "test_contents"
    writer = "test_writer"
    password = "test_password"
    Repository().create_board(
        title=title, writer=writer, contents=contents, password=password
    )

    id = 1
    password = "1"

    dto = DeleteBoardDto(
        id=id,
    )

    usecase = DeleteBoardUseCase()

    assert usecase.execute(dto=dto).type == FailureType.UNAUTHORIZED_ERROR
