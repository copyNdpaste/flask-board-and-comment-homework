from app.extensions.utils.log_helper import logger_
from core.repository.repository import Repository

logger = logger_.getLogger(__name__)


def notify_keyword_contents(
    _from: str, contents: str, board_id: int, comment_id: int = None
):
    notifier = check_keyword(contents)
    msg = ""
    for writer, keywords in notifier.items():
        for keyword in keywords:
            if _from == "board":
                msg = f"{writer}님이 등록하신 키워드 {keyword}가 게시물 {board_id}에 있습니다"
            elif _from == "comment":
                msg = f"{writer}님이 등록하신 키워드 {keyword}가 게시물 {board_id}의 댓글 {comment_id}에 있습니다"

            logger.info(msg)


def check_keyword(contents: str):
    keywords = Repository().get_keywords()

    notifier = {}
    for keyword in keywords:
        if keyword.keyword in contents:
            notifier[keyword.writer] = []
            notifier[keyword.writer].append(keyword.keyword)

    return notifier
