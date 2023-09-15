from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class SamplesCategory(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Samples(models.Model):
    Author = (
        ('Z', 'ضیائی'),
        ('K', 'کارآموز'),
    )

    name = models.CharField(max_length=250, verbose_name='نام طرح')
    title = models.CharField(max_length=250, verbose_name='عتوان طرح')
    slug = models.SlugField(unique=True, blank=True, verbose_name='اسلاگ')
    category = models.ManyToManyField(SamplesCategory, related_name="samples", verbose_name='دسته بندی')
    author = models.CharField(max_length=1, choices=Author, default='Z', verbose_name="توسط")
    description = CKEditor5Field('توضیحات', config_name='extends')
    video = models.FileField(upload_to='video/samples', verbose_name='ویدیو طرح')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آپدیت')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'طرح'
        verbose_name_plural = 'طرح ها'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Samples, self).save()
