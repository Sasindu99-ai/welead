from vvecon.zorion.db import models

__all__ = ["Currency"]


class Currency(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=3, unique=True)
    symbol = models.CharField(max_length=3, unique=True)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4, default=1)
    is_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    class Meta:
        db_table = "currencies"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_default:
            Currency.objects.filter(is_default=True).update(is_default=False)
        if self.is_active:
            Currency.objects.filter(is_active=True).update(is_active=False)
        super(Currency, self).save(*args, **kwargs)
