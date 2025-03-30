from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from core import settings
from vvecon.zorion.urls import include

urlpatterns = (
    [
        path("superadmin/", admin.site.urls),
        include("apps.authentication.urls"),
        include("apps.settings.urls"),
        include("apps.main.urls"),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {
                "document_root": settings.MEDIA_ROOT,
            },
        ),
    ]
)

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
