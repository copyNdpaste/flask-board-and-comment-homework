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
