from datetime import datetime
from typing import Union

from sqlalchemy import and_

from app.extensions.database import session
from app.extensions.utils.log_helper import logger_
from app.persistence.model.board_model import BoardModel
from app.persistence.model.comment_model import CommentModel
from app.persistence.model.keyword_model import KeywordModel

from core.entity.board_entity import BoardEntity
from core.entity.comment_entity import CommentEntity

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
            logger.error(f"[Repository][get_boards] error : {e}")
            return False

    def update_board(self, id, title, contents) -> bool:
        try:
            session.query(BoardModel).filter_by(id=id).update(
                {
                    "title": title,
                    "contents": contents,
                    "updated_at": datetime.utcnow(),
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

    def create_comment(
        self,
        board_id,
        writer,
        contents,
        parent_id=None,
    ) -> Union[CommentEntity, bool]:
        try:
            comment = CommentModel(
                board_id=board_id, writer=writer, contents=contents, parent_id=parent_id
            )

            session.add(comment)
            session.commit()

            return comment.to_entity()
        except Exception as e:
            logger.error(f"[Repository][create_comment] error : {e}")
            session.rollback()
            return False

    def get_comments(self, id, board_id) -> Union[list[CommentEntity], bool]:
        # id는 페이지상의 맨 마지막 게시글 id + 1. 즉, id가 있으면 id부터 조회하면 됨
        # 댓글 10개 선택, child는 있는거 다 붙이기
        try:
            condition = []
            if id:
                condition.append((CommentModel.id >= id))
            if board_id:
                condition.append(CommentModel.board_id == board_id)

            comments = (
                session.query(CommentModel).filter(and_(True, *condition)).limit(10)
            )

            comment_list = []
            for comment in comments:
                if comment.child:
                    pc = comment.to_entity()
                    pc.child = [
                        child_comment.to_entity() for child_comment in comment.child
                    ]
                    comment_list.append(pc)
                elif not comment.parent_id:
                    pc = comment.to_entity()
                    comment_list.append(pc)

            return comment_list
        except Exception as e:
            logger.error(f"[Repository][get_comments] error : {e}")
            return False

    def get_keywords(self):
        try:
            keywords = session.query(KeywordModel).all()

            return [keyword.to_entity() for keyword in keywords] if keywords else []
        except Exception as e:
            logger.error(f"[Repository][get_keywords] error : {e}")
            return False

    def create_keyword(self, writer, keyword):
        try:
            keyword = KeywordModel(writer=writer, keyword=keyword)

            session.add(keyword)
            session.commit()

            return keyword.to_entity()
        except Exception as e:
            logger.error(f"[Repository][create_keywords] error : {e}")
            session.rollback()
            return False
