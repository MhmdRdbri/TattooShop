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
    slug = models.SlugField(unique=True, verbose_name='اسلاگ')
    category = models.ManyToManyField(SamplesCategory, related_name="samples", verbose_name='دسته بندی')
    author = models.CharField(max_length=1, choices=Author, default='Z', verbose_name="توسط")
    body = CKEditor5Field('توضیحات', config_name='extends')
    image = models.ImageField(upload_to='patterns/')
    video = models.FileField(upload_to='video/samples', verbose_name='ویدیو طرح')
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


class Tags(models.Model):
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Description')
    locale = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:locale')
    type = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:type')
    title = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:title')
    descriptionOg = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:description')
    site_name = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:site_name')
    width = models.PositiveIntegerField(blank=True, null=True, verbose_name='Og:image:width')
    height = models.PositiveIntegerField(blank=True, null=True, verbose_name='Og:image:height')

    class Meta:
        verbose_name = 'Sample Page Tag'
        verbose_name_plural = 'Sanple Page Tags'

    def __str__(self):
        return "Sample Page Tags"
