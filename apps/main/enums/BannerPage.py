from vvecon.zorion.db import models

__all__ = ['BannerPage']


class BannerPage(models.TextChoices):
    HOME = 'home', 'Home'
