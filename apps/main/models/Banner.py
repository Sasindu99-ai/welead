from vvecon.zorion.db import models
from ..enums import BannerPage

__all__ = ['Banner']


class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    primaryButtonText = models.CharField(max_length=255)
    primaryButtonLink = models.CharField(max_length=255)
    secondaryButtonText = models.CharField(max_length=255)
    secondaryButtonLink = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    isActive = models.BooleanField(default=True)
    page = models.CharField(choices=BannerPage.choices, max_length=20, default=BannerPage.HOME)

    @property
    def primaryButtonClassNames(self):
        return "btn-primary"

    @property
    def secondaryButtonClassNames(self):
        return "btn-secondary"
