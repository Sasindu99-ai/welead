import os
import random
import string
from typing import List

import yaml

__all__ = ["Utils"]

from django.contrib.gis.geoip2 import GeoIP2
from icecream import ic
from ipware import get_client_ip


class Utils:
    @staticmethod
    def deepUpdate(base, new):
        for key, value in new.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                Utils.deepUpdate(base[key], value)
            else:
                base[key] = value
        return base

    @staticmethod
    def yamlToDict(value):
        if isinstance(value, str):
            return yaml.load(f"dummy: {value}", Loader=yaml.SafeLoader)["dummy"]
        return value

    @staticmethod
    def groupEnv(prefix: str):
        prefix_len = len(prefix)
        return {
            key[prefix_len:]: Utils.yamlToDict(value)
            for key, value in os.environ.items()
            if key.startswith(prefix)
        }

    @staticmethod
    def camelToUrl(name: str) -> str:
        return "".join(["-" + i.lower() if i.isupper() else i for i in name]).lstrip(
            "-"
        )

    @staticmethod
    def viewToHome(cls_name: str) -> str:
        return Utils.camelToUrl(cls_name.replace("View", ""))

    @staticmethod
    def makeUrl(routes: List[str]):
        while "" in routes:
            routes.remove("")
        return "/".join(routes)

    @staticmethod
    def generatePasscode(length: int = 6) -> str:
        return "".join(random.choices(string.digits, k=length))
        # return '1' * length

    @staticmethod
    def urlToClassName(url: str) -> str:
        if url == "":
            return "Home"
        className = "".join(
            [i[0].upper() + i.lower()[1:] for i in url.split("-")]
        ).replace("/", "_")
        while className.endswith("_"):
            className = className[:-1]
        while className.startswith("_"):
            className = className[1:]
        return className

    @staticmethod
    def urlName(url: str) -> str:
        components = url.split("/")
        if len(components) == 1:
            return url
        if components[-1] == "":
            return components[-2]
        for component in components:
            if component.startswith("<"):
                components[components.index(component)] = "index"
        return "/".join(components)

    @staticmethod
    def getUserCountryCode(request):
        ip, is_routable = get_client_ip(request)
        if ip is None:
            return None
        g = GeoIP2()
        try:
            country_code = ic(g.country(ip))["country_code"]
        except Exception:
            return None
        return country_code
