from core.dto.comment_dto import GetCommentsDto
from core.usecases.get_comments_usecase import GetCommentsUseCase


def test_get_comments_when_comment_is_1_then_success(
    session, create_boards, create_comments
):
    writer = "test_writer"
    create_boards(1, writer)
    create_comments(1, writer, 1)
    dto = GetCommentsDto(id=None, board_id=1)

    usecase = GetCommentsUseCase()

    result = usecase.execute(dto=dto)

    assert result.value[0].id == 1
    assert result.meta is None
    assert result.value[0].child == []


def test_get_comments_when_parent_comment_is_11_and_child_comment_is_11_on_each_parent_comment_then_success(
    session, create_boards, create_comments
):
    writer = "test_writer"
    create_boards(1, writer)
    create_comments(11, writer, 1)
    for i in range(1, 12):
        create_comments(11, writer, 1, i)

    dto = GetCommentsDto(id=None, board_id=1)

    usecase = GetCommentsUseCase()

    result = usecase.execute(dto=dto)

    assert len(result.value) == 10
    assert result.value[0].id == 1

    for i in range(10):
        assert len(result.value[i].child) == 11


def test_get_comments_when_comment_is_21_and_id_is_12_then_success(
    session, create_boards, create_comments
):
    writer = "test_writer"
    id = 12
    create_boards(1, writer)
    create_comments(21, writer, 1)
    for i in range(1, 22):
        create_comments(2, writer, 1, i)

    dto = GetCommentsDto(id=id, board_id=1)

    usecase = GetCommentsUseCase()

    result = usecase.execute(dto=dto)

    assert result.value[0].id == 12
    for i in range(10):
        assert len(result.value[i].child) == 2
