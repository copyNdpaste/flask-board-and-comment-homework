from flask import url_for


def test_when_create_board_then_success(
    client, session, test_request_context, make_header
):
    title = "test_title"
    contents = "test_contents"
    writer = "test_writer"
    password = "test_password"

    headers = make_header()

    dct = dict(title=title, writer=writer, contents=contents, password=password)

    # test code which uses a request context
    with test_request_context:
        response = client.post(
            url_for("api.create_board_view"), headers=headers, json=dct
        )

    assert response.status_code == 200
