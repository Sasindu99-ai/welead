from typing import Optional

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound

from vvecon.zorion.core import Service

from ..models import Page

__all__ = ["PageService"]


class PageService(Service):
    model = Page

    def getBySlug(self, slug: str) -> Optional[Page]:
        try:
            page = self.model.objects.get(slug=slug)
            return page
        except (NotFound, ObjectDoesNotExist):
            return None
