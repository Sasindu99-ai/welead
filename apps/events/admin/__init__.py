from django.contrib import admin
from .EventLabelAdmin import EventLabelAdmin
from .AudienceAdmin import AudienceAdmin
from .SponsorAdmin import SponsorAdmin
from .EventAdmin import EventAdmin
from ..models import EventLabel, Audience, Sponsor, Event

admin.site.register(EventLabel, EventLabelAdmin)
admin.site.register(Audience, AudienceAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Event, EventAdmin)
