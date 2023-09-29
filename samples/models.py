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
        ('ضیائی', 'ضیائی'),
        ('کارآموز', 'کارآموز'),
    )

    name = models.CharField(max_length=250, verbose_name='نام طرح')
    title = models.CharField(max_length=250, verbose_name='عتوان طرح')
    slug = models.SlugField(unique=True, verbose_name='اسلاگ')
    category = models.ManyToManyField(SamplesCategory, related_name="samples", verbose_name='دسته بندی')
    author = models.CharField(max_length=100, choices=Author, default='ضیائی', verbose_name="توسط")
    body = CKEditor5Field('توضیحات', config_name='extends')
    image = models.ImageField(upload_to='patterns/')
    alt = models.CharField(max_length=250, default='Type...')
    video = models.FileField(upload_to='video/samples', verbose_name='ویدیو طرح', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آپدیت')

    # tags
    pagetitle = models.CharField(max_length=500, blank=True, null=True, verbose_name='Title')
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Description')
    canonical = models.CharField(max_length=500, blank=True, null=True, verbose_name='Canonical')
    localeOg = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:locale')
    typeOg = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:type')
    titleOg = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:title')
    descriptionOg = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:description')
    site_name = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:site_name')
    widthOg = models.PositiveIntegerField(blank=True, null=True, verbose_name='Og:image:width')
    heightOg = models.PositiveIntegerField(blank=True, null=True, verbose_name='Og:image:height')
    extratag = CKEditor5Field('تگ های جدید', config_name='extends', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'طرح'
        verbose_name_plural = 'طرح ها'
        ordering = ('-created_at',)


class Comment(models.Model):
    sample = models.ForeignKey(Samples, on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    name = models.CharField(max_length=100, verbose_name='Name')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    email = models.EmailField(max_length=255, verbose_name='Email')
    message = models.TextField(verbose_name='Message')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created_at',)

    def __str__(self):
        return f"Comment by {self.name} on {self.sample.title}"


class Tags(models.Model):
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Description')
    locale = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:locale')
    type = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:type')
    title = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:title')
    descriptionOg = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:description')
    site_name = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:site_name')
    width = models.PositiveIntegerField(blank=True, null=True, verbose_name='Og:image:width')
    height = models.PositiveIntegerField(blank=True, null=True, verbose_name='Og:image:height')
    extratag = CKEditor5Field('تگ های جدید', config_name='extends', blank=True, null=True)

    class Meta:
        verbose_name = 'Sample Page Tag'
        verbose_name_plural = 'Sample Page Tags'

    def __str__(self):
        return "Sample Page Tags"
