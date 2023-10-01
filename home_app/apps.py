from django.apps import AppConfig


class HomeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home_app'

    verbose_name = 'صفحه اصلی'
    verbose_name_plural = 'صفحه اصلی'
