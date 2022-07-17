from typing import Union

from sqlalchemy import and_

from app.extensions.database import session
from app.extensions.utils.log_helper import logger_
from app.extensions.utils.time_helper import get_utc_timestamp
from app.persistence.model.board_model import BoardModel

from core.entity.board_entity import BoardEntity

logger = logger_.getLogger(__name__)


class Repository:
    def create_board(
        self, title, writer, contents, password
    ) -> Union[BoardEntity, bool]:
        try:
            board = BoardModel(
                title=title, writer=writer, contents=contents, password=password
            )

            session.add(board)
            session.commit()

            return board.to_entity()
        except Exception as e:
            logger.error(f"[Repository][create_board] error : {e}")
            session.rollback()
            return False

    def get_board(self, id) -> Union[BoardEntity, bool]:
        try:
            board = session.query(BoardModel).filter_by(id=id).first()

            return board.to_entity() if board else None
        except Exception as e:
            logger.error(f"[Repository][get_board] error : {e}")
            session.rollback()
            return False

    def get_boards(self, id, writer, title) -> Union[list[BoardEntity], bool]:
        # writer or title로 검색, writer, title 둘 다 없으면 전체 최신순으로 조회(페이지네이션)
        # id는 페이지상의 맨 마지막 게시글 id - 1. 즉, id가 있으면 id부터 조회하면 됨
        try:
            condition = []
            if id and writer:
                condition.append(BoardModel.writer == writer)
                condition.append((BoardModel.id <= id))
            elif writer:
                condition.append(BoardModel.writer == writer)
            elif id and title:
                pass
                condition.append(BoardModel.title.like(f"%{title}%"))
                condition.append((BoardModel.id <= id))
            elif title:
                condition.append(BoardModel.title.like(f"%{title}%"))
            elif id:
                condition.append((BoardModel.id <= id))

            boards = (
                session.query(BoardModel)
                .filter(and_(True, *condition))
                .order_by(BoardModel.id.desc())
                .limit(10)
            )

            return [board.to_entity() for board in boards] if boards else []
        except Exception as e:
            logger.error(f"[Repository][get_board] error : {e}")
            session.rollback()
            return False

    def update_board(self, id, title, contents) -> bool:
        try:
            session.query(BoardModel).filter_by(id=id).update(
                {
                    "title": title,
                    "contents": contents,
                    "updated_at": get_utc_timestamp(),
                }
            )

            session.commit()

            return True
        except Exception as e:
            logger.error(f"[Repository][update_board] error : {e}")
            session.rollback()
            return False

    def delete_board(self, id) -> bool:
        try:
            session.query(BoardModel).filter_by(id=id).delete()

            session.commit()

            return True
        except Exception as e:
            logger.error(f"[Repository][delete_board] error : {e}")
            session.rollback()
            return False
