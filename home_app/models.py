from datetime import datetime

from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


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


class Message(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField()
    Phone = models.PositiveIntegerField()
    Message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Name
