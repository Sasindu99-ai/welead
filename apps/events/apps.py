from django.apps import AppConfig

__all__ = ['EventConfig']


class EventConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.events'

    def ready(self):
        from . import signals  # noqa: F401
