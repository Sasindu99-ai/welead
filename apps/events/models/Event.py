from vvecon.zorion.db import models
from .Audience import Audience
from .EventLabel import EventLabel
from .Sponsor import Sponsor

__all__ = ['Event']


class Event(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Event Name')
    slug = models.SlugField(max_length=255, verbose_name='Event Slug', unique=True)
    shortDescription = models.TextField(blank=True, null=True, verbose_name='Event Short Description')
    description = models.TextField(blank=True, null=True, verbose_name='Event Description')
    startDate = models.DateField(blank=True, null=True, verbose_name='Event Start Date')
    venue = models.CharField(max_length=255, verbose_name='Venue', null=True, blank=True)
    cover = models.ImageField(blank=True, null=True, verbose_name='Event Cover')
    labels = models.ManyToManyField(EventLabel, verbose_name='Event Labels', related_name='events')
    sponsors = models.ManyToManyField(Sponsor, verbose_name='Sponsors', related_name='events')
    audiences = models.ManyToManyField(Audience, verbose_name='Audiences', related_name='events')
