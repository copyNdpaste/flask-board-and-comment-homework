from pydantic import BaseModel


class CreateBoardDto(BaseModel):
    title: str = None
    contents: str = None
    writer: str = None
    password: str = None


class UpdateBoardDto(BaseModel):
    id: int = None
    title: str = None
    contents: str = None
    password: str = None


class DeleteBoardDto(BaseModel):
    id: int = None
    password: str = None
