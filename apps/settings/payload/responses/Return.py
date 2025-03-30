from typing import Any

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)

__all__ = ["Return"]


class Return:
    @staticmethod
    def ok(content: Any = True) -> Response:
        return Response(data=content, status=HTTP_200_OK)

    @staticmethod
    def created(content: Any = True) -> Response:
        return Response(data=content, status=HTTP_201_CREATED)

    @staticmethod
    def notFound(content: Any = False) -> Response:
        return Response(data=content, status=HTTP_404_NOT_FOUND)

    @staticmethod
    def badRequest(content: Any = False) -> Response:
        return Response(data=content, status=HTTP_400_BAD_REQUEST)
