from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دوره")
    media = models.FileField(upload_to='images/course', blank=True, null=True)
    alt = models.CharField(max_length=100, verbose_name='Alt', blank=True, null=True)
    body = CKEditor5Field('Text', config_name='extends', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, verbose_name='Slug')

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

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = "دوره ها"

    def __str__(self):
        return self.name


class CourseAttribute(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, verbose_name="نام ویژگی")
    value = models.CharField(max_length=255, verbose_name="مقدار ویژگی")

    def __str__(self):
        return f"{self.course.name} - {self.key}: {self.value}"

    class Meta:
        verbose_name = 'ویژگی'
        verbose_name_plural = "ویژگی ها"


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
        verbose_name = 'Course Page Tag'
        verbose_name_plural = 'Course Page Tags'

    def __str__(self):
        return "Course Page Tags"
