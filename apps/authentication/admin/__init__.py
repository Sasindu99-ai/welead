from django.contrib import admin

from ..models import User
from .UserAdmin import UserAdmin

admin.site.register(User, UserAdmin)
