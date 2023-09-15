from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Samples(models.Model):
    Author = (
        ('Z', 'ضیائی'),
        ('K', 'کارآموز'),
    )

    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=1, choices=Author, default='Z')
    description = CKEditor5Field('Text', config_name='extends')
    video = models.FileField(upload_to='video/samples')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name