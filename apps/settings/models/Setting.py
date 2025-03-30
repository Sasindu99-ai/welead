import json

from vvecon.zorion.db import models

__all__ = ["Setting", "DataType"]


class DataType(models.TextChoices):
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    JSON = "json"


class Setting(models.Model):
    tag = models.CharField(max_length=255, blank=True, null=True)
    key = models.CharField(max_length=255)
    value = models.TextField()
    data_type = models.TextField(choices=DataType.choices, default=DataType.STRING)

    class Meta:
        db_table = "settings"
        ordering = ["key"]

    def __str__(self):
        return self.key

    def getValue(self):
        if self.data_type == DataType.STRING:
            return self.value
        elif self.data_type == DataType.INTEGER:
            return int(self.value)
        elif self.data_type == DataType.FLOAT:
            return float(self.value)
        elif self.data_type == DataType.BOOLEAN:
            return self.value.lower() == "true"
        elif self.data_type == DataType.JSON:
            return json.loads(self.value)
        else:
            raise ValueError("Invalid data type")
