from pydantic import BaseModel


class KeywordEntity(BaseModel):
    id: int = None
    writer: str = None
    keyword: str = None
