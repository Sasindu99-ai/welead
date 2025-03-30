from dataclasses import dataclass
from enum import Enum
from typing import Any, Type

from .Files import FileMaker
from .Theme import ThemeFolder

__all__ = ["Images", "Image"]


@dataclass
class Image:
    path: str
    url: str
    alt: str = ""
    classList: str = ""
    style: str = ""
    width: str = ""
    height: str = ""
    elementId: str = ""

    def __str__(self):
        return self.alt


class Images:
    __theme__: Type[Enum] | Enum
    images: FileMaker = NotImplemented

    def __init__(self, theme: Type[Enum] | Enum):
        self.__theme__ = theme

        self.createImages()

    def createImages(self):
        if self.images is not NotImplemented and isinstance(self.images, FileMaker):
            for file_name in self.images.__dict__:
                file = self.images.__getattribute__(file_name)
                if isinstance(file, str):
                    file = (file, 1)
                self.createImage(file, file_name)

    def createImage(self, file: tuple, file_name: str):
        file_path = file[0]
        version = file[1] if len(file) > 1 else 1
        folder = file[2] if len(file) > 2 else ThemeFolder.common
        data = file[3] if len(file) > 3 else False

        if not getattr(self, file_name, False):
            setattr(
                self,
                file_name,
                Image(
                    *self.imageFile(file_path, version, folder, data=True),
                    **(data if data else {}),
                ),
            )

    def imageFile(
        self,
        file: str,
        version: int,
        folder: Any,
        urlOnly: bool = False,
        data: bool = False,
    ) -> str | tuple:
        if folder == ThemeFolder.theme:
            folder = self.__theme__
        file = f"img/{folder.value}/{file}"
        if data:
            return (
                file,
                file + f"?v={version}",
                file.split("/")[-1].split(".")[0].replace("-", " ").title(),
            )
        if urlOnly:
            return file, (file + f"?v={version}",)
        return file, '<img src="{0}" alt="{1}">'.format(
            "{% static " + file + f"?v={version}" + " %}",
            file.split("/")[-1].split(".")[0].replace("-", " ").title(),
        )
