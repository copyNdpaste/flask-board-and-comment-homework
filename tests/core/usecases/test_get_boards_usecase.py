from core.dto.board_dto import GetBoardsDto
from core.usecases.get_boards_usecase import GetBoardsUseCase


def test_get_boards_when_board_is_1_then_success(session, create_boards):
    writer = "test_writer"
    create_boards(1, writer)

    dto = GetBoardsDto(writer=writer)

    usecase = GetBoardsUseCase()

    result = usecase.execute(dto=dto)

    assert result.value[0].id == 1
    assert result.meta == 0


def test_get_boards_by_writer_when_board_is_21_and_id_is_12_then_success(
    session, create_boards
):
    writer = "test_writer"
    id = 11
    create_boards(21, writer)

    dto = GetBoardsDto(id=id, writer=writer)

    usecase = GetBoardsUseCase()

    result = usecase.execute(dto=dto)

    assert result.value[0].id == 11
    assert result.value[0].title == "test_title11"
    assert result.value[0].writer == writer

    assert result.value[9].id == 2
    assert result.value[9].title == "test_title2"
    assert result.value[9].writer == writer


def test_get_boards_by_title_when_board_is_21_and_id_is_12_then_success(
    session, create_boards
):
    writer = "test_writer"
    id = 11
    create_boards(21, writer)

    dto = GetBoardsDto(id=id, title="test_title")

    usecase = GetBoardsUseCase()

    result = usecase.execute(dto=dto)

    assert result.value[0].id == 11
    assert result.value[0].title == "test_title11"
    assert result.value[0].writer == writer

    assert result.value[9].id == 2
    assert result.value[9].title == "test_title2"
    assert result.value[9].writer == writer
