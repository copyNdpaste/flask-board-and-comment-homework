from sqlalchemy import (
    Column,
    Integer,
    String,
)

from app import db
from core.entity.keyword_entity import KeywordEntity


class KeywordModel(db.Model):
    __tablename__ = "keywords"

    id = Column(Integer(), primary_key=True)
    keyword = Column(String(50), nullable=False)
    writer = Column(String(30), nullable=False)

    def to_entity(self) -> KeywordEntity:
        return KeywordEntity(
            id=self.id,
            keyword=self.keyword,
            writer=self.writer,
        )
