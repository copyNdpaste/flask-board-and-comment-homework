from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app import db
from app.extensions.utils.time_helper import get_utc_timestamp
from app.persistence.model.board_model import BoardModel

from core.entity.comment_entity import CommentEntity


class CommentModel(db.Model):
    __tablename__ = "comments"

    id = Column(Integer(), primary_key=True)
    contents = Column(String(1000), nullable=False)
    writer = Column(String(30), nullable=False)
    parent_id = Column(Integer(), ForeignKey("comments.id"), nullable=True)
    board_id = Column(Integer(), ForeignKey(BoardModel.id), nullable=False)
    created_at = Column(String(10), default=get_utc_timestamp(), nullable=False)

    board = relationship("BoardModel", backref="comments")
    parent = relationship("CommentModel", remote_side=[id], backref="child")

    def to_entity(self) -> CommentEntity:
        return CommentEntity(
            id=self.id,
            contents=self.contents,
            writer=self.writer,
            parent_id=self.parent_id,
            board_id=self.board_id,
            created_at=self.created_at,
            child=[],
        )
