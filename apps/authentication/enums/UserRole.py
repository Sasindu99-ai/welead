from vvecon.zorion.db import models

__all__ = ["UserRole"]


class UserRole(models.TextChoices):
    STUDENT = "Student"
    TEACHER = "Teacher"
    PARENT = "Parent"
    ALUMNI = "Alumni"
    GUEST = "Guest"
