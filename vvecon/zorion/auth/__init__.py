import inspect
from functools import wraps
from os import environ
from typing import Optional

from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from icecream import ic
from rest_framework import status
from rest_framework.response import Response

from .JWTProvider import JWTProvider

__all__ = ["Authorized", "Authenticated", "JWTProvider"]


def Authorize(
    authorized: Optional[bool] = None, staff: bool = False, admin: bool = False
):
    def Auth(func):
        sig = inspect.signature(func)
        params = list(sig.parameters.values())

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            request = kwargs.get("request", None)
            ic([request, staff, admin])
            if request is None and authorized:
                return Response(
                    {"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED
                )
            if not request.user.is_authenticated and authorized:
                return Response(
                    {"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED
                )
            if authorized:
                ic([request.user, request.user.is_staff, request.user.is_superuser])
                if not (
                    (staff and request.user.is_staff)
                    or (admin and request.user.is_superuser)
                    or (not staff and not admin)
                ):
                    raise PermissionDenied("Unauthorized")
            parameters = inspect.signature(func).parameters
            if "request" in parameters:
                return func(self, *args, **kwargs)
            kwargs.pop("request")
            return func(self, *args, **kwargs)

        if "request" not in [param.name for param in params]:
            params.append(
                inspect.Parameter("request", inspect.Parameter.POSITIONAL_OR_KEYWORD)
            )
        if hasattr(wrapper, "__signature__"):
            wrapper.__signature__ = sig.replace(parameters=params)
        return wrapper

    return Auth


def Authenticate(staff=False, admin=False):
    def Auth(func):
        sig = inspect.signature(func)
        params = list(sig.parameters.values())

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            request = kwargs.get("request", None)
            if request is None and (staff or admin):
                raise PermissionDenied("Unauthorized")
            if not request.user.is_authenticated and (staff or admin):
                return redirect(
                    environ.get("AUTH_ADMIN_URL")
                    if request.path.startswith("/admin/")
                    else environ.get("AUTH_URL")
                )
            if not (
                (staff and request.user.is_staff)
                or (admin and request.user.is_superuser)
                or (not staff and not admin)
            ):
                raise PermissionDenied("Unauthorized")
            parameters = inspect.signature(func).parameters
            if "request" in parameters:
                return func(self, *args, **kwargs)
            kwargs.pop("request")
            return func(self, *args, **kwargs)

        if "request" not in [param.name for param in params]:
            params.append(
                inspect.Parameter("request", inspect.Parameter.POSITIONAL_OR_KEYWORD)
            )
        wrapper.__signature__ = sig.replace(parameters=params)
        return wrapper

    return Auth


Authorized = Authorize
Authenticated = Authenticate
