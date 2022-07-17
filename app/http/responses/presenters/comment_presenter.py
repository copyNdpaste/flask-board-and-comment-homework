from typing import Union

from pydantic import ValidationError

from app.extensions.utils.log_helper import logger_
from app.http.responses import failure_response, success_response
from core.schema.comment_schema import GetCommentsResponseSchema

from core.usecase_output import UseCaseSuccessOutput, UseCaseFailureOutput, FailureType

logger = logger_.getLogger(__name__)


class CreateCommentPresenter:
    def transform(self, output: Union[UseCaseSuccessOutput, UseCaseFailureOutput]):
        if isinstance(output, UseCaseSuccessOutput):
            value = output.value
            result = {
                "data": value,
                "meta": output.meta,
            }
            return success_response(result=result)
        elif isinstance(output, UseCaseFailureOutput):
            return failure_response(output=output)


class GetCommentsPresenter:
    def transform(self, output: Union[UseCaseSuccessOutput, UseCaseFailureOutput]):
        if isinstance(output, UseCaseSuccessOutput):
            value = output.value
            if value:
                try:
                    schema = GetCommentsResponseSchema(comments=value)
                except ValidationError as e:
                    logger.error(f"[GetCommentsPresenter][transform] error : {e}")
                    return failure_response(
                        UseCaseFailureOutput(
                            type=FailureType.SYSTEM_ERROR,
                            message="response schema validation error",
                        )
                    )
            result = {
                "data": schema.dict() if value else {"comments": []},
                "meta": output.meta,
            }
            return success_response(result=result)
        elif isinstance(output, UseCaseFailureOutput):
            return failure_response(output=output)
