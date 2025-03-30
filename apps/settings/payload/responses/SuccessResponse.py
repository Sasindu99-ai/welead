from typing import Any

from vvecon.zorion import serializers

__all__ = ["SuccessResponse"]


class SuccessResponse(serializers.Response):
    def __init__(self, message: Any = True, data=None):
        if data is None:
            data = dict()
        super().__init__(message=message, data=data)
