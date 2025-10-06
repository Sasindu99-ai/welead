from vvecon.zorion.urls import django_include, django_path, paths

from .views import HomeView, PageView, AboutUsView, ContactUsView

urlpatterns = paths([HomeView, PageView, AboutUsView, ContactUsView]) + [
    django_path("auth/", django_include("allauth.urls")),
]
