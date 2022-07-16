from core.dto.board_dto import CreateBoardDto
from core.usecase_output import UseCaseSuccessOutput


class CreateBoardUseCase:
    def execute(self, dto:CreateBoardDto):
        print('CreateBoardUseCase')

        return UseCaseSuccessOutput(value=True)