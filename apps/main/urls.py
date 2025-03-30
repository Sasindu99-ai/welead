from vvecon.zorion.urls import django_include, django_path, paths

from .views import HomeView, PageView

urlpatterns = paths([HomeView, PageView]) + [
    django_path("auth/", django_include("allauth.urls")),
]
