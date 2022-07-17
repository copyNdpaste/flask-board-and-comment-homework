from flask import url_for


def test_when_create_comment_then_success(
    client, session, test_request_context, make_header, create_boards
):
    contents = "test_contents"
    writer = "test_writer"
    board_id=1

    create_boards(1, writer)

    headers = make_header()

    dct = dict(board_id=board_id, writer=writer, contents=contents, )

    # test code which uses a request context
    with test_request_context:
        response = client.post(
            url_for("api.create_comment_view"), headers=headers, json=dct
        )

    assert response.status_code == 200


# def test_when_get_board_then_success(
#     client, session, test_request_context, make_header, create_boards
# ):
#     writer = "test_writer"
#     id = 11
#     create_boards(21, writer)
#
#     headers = make_header()
#
#     dct = dict(id=11, writer=writer, title=None)
#
#     # test code which uses a request context
#     with test_request_context:
#         response = client.get(url_for("api.get_boards_view"), headers=headers, json=dct)
#
#     assert response.status_code == 200
#     assert response.json["data"]["boards"][0]["id"] == 11
#     assert response.json["data"]["boards"][-1]["id"] == 2
#     assert response.json["meta"] == 1
