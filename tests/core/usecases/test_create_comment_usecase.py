from core.dto.comment_dto import CreateCommentDto
from core.usecase_output import FailureType
from core.usecases.create_comment_usecase import CreateCommentUseCase


def test_create_comment_then_success(session, create_boards):
    writer = "test_writer"

    create_boards(1, writer)

    dto = CreateCommentDto(contents="hi", writer=writer, board_id=1)

    usecase = CreateCommentUseCase()

    assert usecase.execute(dto=dto).value


def test_when_create_comment_with_wrong_params_then_fail(session, create_boards):
    writer = "test_writer"

    create_boards(1, writer)

    dto = CreateCommentDto(contents="hi", writer=writer, board_id=None)

    usecase = CreateCommentUseCase()

    assert usecase.execute(dto=dto).type == FailureType.INVALID_REQUEST_ERROR
