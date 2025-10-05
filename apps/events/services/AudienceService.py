from vvecon.zorion.core import Service
from ..models import Audience

__all__ = ['AudienceService']


class AudienceService(Service):
    model = Audience
