from flask import Blueprint


api: Blueprint = Blueprint(name="api", import_name=__name__)

from .board_view import *  # noqa isort:skip
from .comment_view import *  # noqa isort:skip
