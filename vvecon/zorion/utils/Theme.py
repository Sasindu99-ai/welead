from enum import Enum

__all__ = ["Theme", "ThemeFolder"]


class Theme(Enum):
    light = "light"
    dark = "dark"


class ThemeFolder(Enum):
    common = "common"
    theme = "theme"
