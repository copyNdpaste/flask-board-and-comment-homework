from typing import Union

from app.extensions.database import session
from app.extensions.utils.log_helper import logger_
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

    def update_board(self, id, title, contents) -> bool:
        try:
            session.query(BoardModel).filter_by(id=id).update(
                {"title": title, "contents": contents}
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
