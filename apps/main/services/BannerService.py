from vvecon.zorion.core import Service
from ..models import Banner

__all__ = ['BannerService']


class BannerService(Service):
    model = Banner
    filterableFields = ('page', )
