from enum import Enum
from typing import Type

from .Data import Data
from .Files import Files
from .Images import Images
from .Theme import Theme

__all__ = ["R"]


class R:
    __theme__: Type[Enum] | Enum

    data: Data
    files: Files
    images: Images

    def __init__(self, theme: Type[Enum] | Enum = Theme.light):
        self.__theme__ = theme

        self.data = Data()
        self.files = Files(self.__theme__)
        self.images = Images(self.__theme__)
