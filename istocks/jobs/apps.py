import os
from django.apps import AppConfig


class JobsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jobs'

    def ready(self):
        from . import updater
        if os.environ.get('RUN_MAIN'):
            updater.start()
