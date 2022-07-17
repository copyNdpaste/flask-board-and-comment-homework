from core.repository.repository import Repository


def test_create_board_then_success(session):
    title = "test_title"
    contents = "test_contents"
    writer = "test_writer"
    password = "test_password"

    result = Repository().create_board(
        title=title, writer=writer, contents=contents, password=password
    )

    assert result.title == title


def test_update_board_then_success(session):
    title = "test_title"
    contents = "test_contents"
    writer = "test_writer"
    password = "test_password"

    Repository().create_board(
        title=title, writer=writer, contents=contents, password=password
    )

    id = "1"
    title_2 = "test_title_2"
    contents_2 = "test_contents_2"

    Repository().update_board(
        id=id,
        title=title_2,
        contents=contents_2,
    )

    result = Repository().get_board(id)

    assert result.title == title_2
    assert result.contents == contents_2


def test_delete_board_then_success(session):
    title = "test_title"
    contents = "test_contents"
    writer = "test_writer"
    password = "test_password"

    Repository().create_board(
        title=title, writer=writer, contents=contents, password=password
    )

    id = "1"

    Repository().delete_board(
        id=id,
    )

    result = Repository().get_board(id)

    assert result == None


def test_get_boards_by_writer_when_board_is_1_then_success(session, create_boards):
    writer = "test_writer"
    create_boards(1, writer)

    boards = Repository().get_boards(None, writer, None)

    assert boards[0].id == 1
    assert boards[0].title == "test_title1"


def test_get_boards_by_writer_when_board_is_11_then_success(session, create_boards):
    writer = "test_writer"
    create_boards(11, writer)

    boards = Repository().get_boards(None, writer, None)

    assert boards[0].id == 11
    assert boards[0].title == "test_title11"

    assert boards[9].id == 2
    assert boards[9].title == "test_title2"


def test_get_boards_by_writer_when_board_is_21_and_id_is_12_then_success(
    session, create_boards
):
    writer = "test_writer"
    create_boards(21, writer)

    boards = Repository().get_boards(11, writer, None)

    assert boards[0].id == 11
    assert boards[0].title == "test_title11"

    assert boards[9].id == 2
    assert boards[9].title == "test_title2"


def test_get_boards_by_title_when_board_is_1_then_success(session, create_boards):
    writer = "test_writer"
    create_boards(1, writer)

    boards = Repository().get_boards(None, None, "test_title")

    assert boards[0].id == 1
    assert boards[0].title == "test_title1"


def test_get_boards_by_title_when_board_is_11_then_success(session, create_boards):
    writer = "test_writer"
    create_boards(11, writer)

    boards = Repository().get_boards(None, None, "test_title")

    assert boards[0].id == 11
    assert boards[0].title == "test_title11"

    assert boards[9].id == 2
    assert boards[9].title == "test_title2"


def test_get_boards_by_title_when_board_is_21_and_id_is_12_then_success(
    session, create_boards
):
    writer = "test_writer"
    create_boards(21, writer)

    boards = Repository().get_boards(11, None, "test_title")

    assert boards[0].id == 11
    assert boards[0].title == "test_title11"

    assert boards[9].id == 2
    assert boards[9].title == "test_title2"
