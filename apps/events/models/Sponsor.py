from vvecon.zorion.db import models

__all__ = ['Sponsor']


class Sponsor(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Sponsor Name')
    logo = models.ImageField(upload_to='sponsors/', blank=True, null=True, verbose_name='Sponsor Logo')
    website = models.URLField(blank=True, null=True, verbose_name='Sponsor Website')
    description = models.TextField(blank=True, null=True, verbose_name='Sponsor Description')
