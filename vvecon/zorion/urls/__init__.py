from typing import Type

from django.urls import include as django_include
from django.urls import path as django_path

from vvecon.zorion.views import API, View

__all__ = ["path", "paths", "include", "django_path", "django_include"]


def path(view: Type[View] | Type[API], app_name: str = NotImplemented) -> list:
    return view().generateURLPatterns(app_name=app_name)


def paths(views: list[Type[View] | Type[API]], app_name: str = NotImplemented) -> list:
    urlpatterns = []
    for view in views:
        urlpatterns += view().generateURLPatterns(app_name=app_name)
    return urlpatterns


def include(appUrls: str) -> list:
    return django_path("", django_include(appUrls))
