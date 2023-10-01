from datetime import datetime
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Message(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True, verbose_name='نام')
    Email = models.EmailField(verbose_name='ایمیل')
    Phone = models.CharField(max_length=15, verbose_name='شماره همراه')
    Message = models.TextField(verbose_name='پیام')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'
        ordering = ('-created_at',)


class ExtraTags(models.Model):
    field = models.TextField(blank=True, null=True, verbose_name="تگ های جدید")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return 'تگ های جدید'

    class Meta:
        verbose_name = 'تگ جدید'
        verbose_name_plural = 'تگ های جدید'
        ordering = ('-created_at',)


class Schema(models.Model):
    schema1 = models.TextField(blank=True, null=True, verbose_name="اسکیما")
    schema2 = models.TextField(blank=True, null=True, verbose_name="اسکیما")

    def __str__(self):
        return 'اسکیما'

    class Meta:
        verbose_name = 'اسکیما'
        verbose_name_plural = 'اسکیما ها'
