from django.contrib import admin
from .BannerAdmin import BannerAdmin
from ..models import Banner

admin.site.register(Banner, BannerAdmin)
