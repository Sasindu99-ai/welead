from vvecon.zorion.core import Service
from ..models import Event
from django.utils.timezone import now

__all__ = ['EventService']


class EventService(Service):
    model = Event

    def getUpcomingEvent(self) -> Event | None:
        return self.model.objects.filter(startDate__gte=now()).order_by('startDate').first()
