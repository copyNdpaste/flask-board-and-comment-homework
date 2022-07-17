from flask import url_for


def test_when_create_comment_then_success(
    client, session, test_request_context, make_header, create_boards
):
    contents = "test_contents"
    writer = "test_writer"
    board_id = 1

    create_boards(1, writer)

    headers = make_header()

    dct = dict(
        board_id=board_id,
        writer=writer,
        contents=contents,
    )

    # test code which uses a request context
    with test_request_context:
        response = client.post(
            url_for("api.create_comment_view"), headers=headers, json=dct
        )

    assert response.status_code == 200


def test_when_get_boards_then_success(
    client, session, test_request_context, make_header, create_boards, create_comments
):
    writer = "test_writer"
    id = 12
    create_boards(1, writer)
    create_comments(21, writer, 1)
    for i in range(1, 22):
        create_comments(2, writer, 1, i)

    headers = make_header()

    dct = dict(id=id, board_id=1)

    # test code which uses a request context
    with test_request_context:
        response = client.get(
            url_for("api.get_comments_view"), headers=headers, json=dct
        )

    assert response.status_code == 200
    assert response.json["data"]["comments"][0]["id"] == 12
    assert response.json["meta"] == 22
    for i in range(10):
        assert len(response.json["data"]["comments"][i]["child"]) == 2
