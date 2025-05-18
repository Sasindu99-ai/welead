from django.core.exceptions import ObjectDoesNotExist, SynchronousOnlyOperation
from django.db.utils import OperationalError
from icecream import ic
from rest_framework.exceptions import NotFound

from vvecon.zorion.core import Service

from ..models import Setting

__all__ = ["SettingService"]


class SettingService(Service):
    model = Setting

    def getByKeys(self, keys: list[str], tag: str = "", default=NotImplemented):
        try:
            settings = self.model.objects.filter(key__in=keys, tag=tag)
            if not settings and default is NotImplemented:
                raise KeyError(f"Settings with keys '{keys}' not found")
            elif not settings:
                return default
            orderedList = []
            for key in keys:
                setting = settings.filter(key=key).first()
                if setting is not None:
                    orderedList.append(setting.getValue())
                else:
                    orderedList.append(None)
            return orderedList
        except (
            ObjectDoesNotExist,
            NotFound,
            OperationalError,
            SynchronousOnlyOperation,
        ) as e:
            ic(e)
            if default is NotImplemented:
                raise KeyError(f"Settings with keys '{keys}' not found")
            return default

    def getByKey(self, key: str, tag: str = "", default=NotImplemented):
        try:
            setting: Setting = self.model.objects.filter(key=key, tag=tag).first()
            if setting is None and default is NotImplemented:
                raise KeyError(f"Setting with key '{key}' not found")
            elif setting is None:
                return default
            return setting.getValue()
        except (
            ObjectDoesNotExist,
            NotFound,
            OperationalError,
            SynchronousOnlyOperation,
        ) as e:
            ic(e)
            if default is NotImplemented:
                raise KeyError(f"Setting with key '{key}' not found")
            return default

    async def getAsyncByKey(self, key: str, tag: str = "", default=NotImplemented):
        try:
            setting: Setting = await self.model.objects.filter(key=key, tag=tag).first()
            if setting is None and default is NotImplemented:
                raise KeyError(f"Setting with key '{key}' not found")
            elif setting is None:
                return default
            return setting.getValue()
        except (
            ObjectDoesNotExist,
            NotFound,
            OperationalError,
            SynchronousOnlyOperation,
        ) as e:
            ic(e)
            if default is NotImplemented:
                raise KeyError(f"Setting with key '{key}' not found")
            return default
