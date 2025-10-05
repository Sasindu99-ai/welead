from vvecon.zorion.db import models

__all__ = ['EventLabel']


class EventLabel(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Label Name')
    color = models.CharField(max_length=9, verbose_name='Label Color')

    def __str__(self):
        return self.name
