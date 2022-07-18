from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)

from app import db

from core.entity.board_entity import BoardEntity


class BoardModel(db.Model):
    __tablename__ = "boards"

    id = Column(Integer(), primary_key=True)
    title = Column(String(50), index=True, nullable=False)
    contents = Column(String(10000), nullable=False)
    writer = Column(String(30), index=True, nullable=False)
    password = Column(String(10), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def to_entity(self) -> BoardEntity:
        return BoardEntity(
            id=self.id,
            title=self.title,
            contents=self.contents,
            writer=self.writer,
            password=self.password,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
