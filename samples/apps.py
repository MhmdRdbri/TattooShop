from django.apps import AppConfig


class SamplesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'samples'

    verbose_name = 'نمونه کار'
    verbose_name_plural = 'نمونه کار ها'
    ordering = ('-created',)
