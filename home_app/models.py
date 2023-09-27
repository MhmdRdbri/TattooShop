from datetime import datetime
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Message(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField()
    Phone = models.CharField(max_length=15, verbose_name='Phone')
    Message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Name


class ExtraTags(models.Model):
    field = CKEditor5Field('تگ های جدید', config_name='extends', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return 'Extra Tags'


class Schema(models.Model):
    schema1 = CKEditor5Field('اسکیما', config_name='extends', blank=True, null=True)
    schema2 = CKEditor5Field('اسکیما', config_name='extends', blank=True, null=True)

    def __str__(self):
        return 'Schema Code'
