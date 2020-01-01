from django.apps import AppConfig


class CoreAppConfig(AppConfig):
    name = 'core_app'

    def ready(self):
        from . import expire
        return super().ready()
