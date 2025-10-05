from vvecon.zorion.db import models

__all__ = ['Audience']


class Audience(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Audience Name')
    description = models.TextField(blank=True, null=True, verbose_name='Audience Description')

    def __str__(self):
        return self.name
