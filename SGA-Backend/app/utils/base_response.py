from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel

T = TypeVar('T')

class BaseResponse(BaseModel, Generic[T]):
    ok: bool
    message: str
    data: Optional[T] = None

    @classmethod
    def success_response(cls, data: Any = None, message: str = "Operation successful"):
        return cls(
            ok=True,
            message=message,
            data=data
        )

    @classmethod
    def error_response(cls, message: str = "Operation failed"):
        return cls(
            ok=False,
            message=message,
        )