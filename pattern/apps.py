from django.apps import AppConfig


class PatternConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pattern'

    verbose_name = 'طرح پیشنهادی'
    verbose_name_plural = 'طرح های پیشنهادی'
