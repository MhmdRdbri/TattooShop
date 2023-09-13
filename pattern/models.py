from django.db import models


class Pattern(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = CKEditor5Field('Text', config_name='extends')
    media = models.FileField(upload_to='patterns/')
    alt = models.CharField(max_length=100, verbose_name='Alt', default='Alt')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return f"{self.title}"