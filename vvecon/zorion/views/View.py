import inspect
import logging
import secrets
from typing import Dict, Type

from django import views
from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist
from django.urls import path as django_path
from django.utils.safestring import mark_safe
from django.utils.translation import get_language_info
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.settings import api_settings

from vvecon.zorion.app import settings
from vvecon.zorion.enums import Method
from vvecon.zorion.utils import R, Utils

__all__ = ["View"]


class View:
    exclude = ["generateURLPatterns", "callView", "getPermissions", "render", "__404__"]
    views: Dict = dict()
    permissions: Dict = dict()
    base: str = ""
    R: R
    context: Dict = dict()

    @classmethod
    def getRequestParser(cls, params) -> Type[Serializer] | None:
        try:
            for value in params.values():
                if issubclass(value.annotation, (Serializer, ModelSerializer)):
                    return value.annotation
            return None
        except TypeError:
            return None

    def callView(self, func, method):
        def viewFunc(viewSelf, request, *args, **kwargs):
            params = inspect.signature(func).parameters
            if len(params) > 0:
                requestParser = self.getRequestParser(params)
                if requestParser is not None and issubclass(
                    requestParser, (Serializer, ModelSerializer)
                ):
                    parser = requestParser(
                        data=request.GET if method == Method.GET else request.POST
                    )
                    if parser.is_valid(raise_exception=False):
                        pass
                    for key, value in parser.validated_data.items():
                        setattr(parser, key, value)
                    if "request" in params:
                        return func(*args, data=parser, request=request, **kwargs)
                    else:
                        return func(*args, data=parser, **kwargs)
                elif "request" in params:
                    return func(*args, request=request, **kwargs)
            return func(*args, **kwargs)

        return viewFunc

    def getPermissions(self, className: str, request) -> list:
        if (
            className in self.permissions.keys()
            and request.method.lower() in self.permissions[className].keys()
        ):
            return self.permissions[className][request.method.lower()]
        return []

    def generateURLPatterns(self, app_name: str = NotImplemented):
        self.views = dict()
        funcs = [
            func
            for func in dir(self)
            if not func.startswith("__")
            and func not in self.exclude
            and callable(getattr(self, func))
        ]

        for fn in funcs:
            func = getattr(self, fn)
            if hasattr(func, "method") and hasattr(func, "path"):
                # Extract method and path from function
                method = func.method
                path = func.path
                authorized = getattr(func, "authorized", False)

                # Create view class if not already in views
                if path not in self.views.keys():
                    self.views[path] = type(
                        Utils.urlToClassName(path),
                        (views.View,),
                        {
                            "authentication_classes": [
                                SessionAuthentication,
                                TokenAuthentication,
                            ]
                            + api_settings.DEFAULT_AUTHENTICATION_CLASSES,
                            "get_permissions": lambda viewSelf: self.getPermissions(
                                Utils.urlToClassName(path), viewSelf.request
                            ),
                        },
                    )
                    self.permissions[Utils.urlToClassName(path)] = dict()
                permissions = self.permissions[Utils.urlToClassName(path)].get(
                    method.name.lower(), []
                )
                if authorized:
                    permissions.append(IsAuthenticated())
                else:
                    permissions.append(AllowAny())
                self.permissions[Utils.urlToClassName(path)][method.name.lower()] = (
                    permissions
                )

                setattr(
                    self.views[path], method.name.lower(), self.callView(func, method)
                )
        # generate urls from views
        return [
            django_path(
                self.base + url,
                view.as_view(),
                name=Utils.urlName(
                    (app_name + ":" if app_name is not NotImplemented else "")
                    + self.base
                    + url
                ),
            )
            for url, view in self.views.items()
        ]

    def render(
        self,
        request,
        context: dict = NotImplemented,
        template_name: str = NotImplemented,
    ):
        if context is NotImplemented:
            context = {}

        for key, value in self.context.items():
            if key not in context:
                context[key] = value

        context["nonce"] = mark_safe(f"{secrets.token_hex(16)}")
        context["R"] = self.R
        context["DEBUG"] = getattr(settings, "DEBUG", False)
        context["LANGUAGE_CODE"] = getattr(settings, "LANGUAGE_CODE", "en-us")
        context["LANGUAGE_NAME"] = get_language_info(
            getattr(settings, "LANGUAGE_CODE", {"name_local": "English"})
        ).get("name_local", "English")

        try:
            return render(request, template_name + ".html", context)
        except TemplateDoesNotExist as e:
            logging.error(e)
            return HttpResponseNotAllowed([request.method])

    @classmethod
    def __404__(cls, request, template_name: str = "404.html"):
        return render(request, template_name, status=404)
