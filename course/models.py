from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دوره")
    href = models.CharField(max_length=100, verbose_name='کلاس', default='Type...')
    cover = models.FileField(upload_to='images/cover/course', verbose_name="کاور ویدئو")
    media = models.FileField(upload_to='videos/course', verbose_name="ویدئو")
    image = models.ImageField(upload_to='images/course', default=cover, verbose_name="نصویر")
    duration = models.CharField(max_length=200, default='Type...', verbose_name="مدت زمان فیلم")
    alt = models.CharField(max_length=100, verbose_name='جایگزین عکس', blank=True, null=True)
    body = CKEditor5Field('متن', config_name='extends', blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=100, verbose_name="نامک")
    created_at = models.DateTimeField(auto_now_add=True)

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
    Index = (
        ('index', 'index'),
        ('noindex', 'noindex'),

    )
    Follow = (
        ('follow', 'follow'),
        ('nofollow', 'nofollow'),

    )
    index_noindex = models.CharField(max_length=150, choices=Index, default='index')
    follow_nofollow = models.CharField(max_length=150, choices=Follow, default='follow')
    twitter_title = models.CharField(max_length=500, blank=True, null=True, verbose_name='Twitter:title')
    twitter_description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Twitter:description')
    extratag = models.TextField(blank=True, null=True, verbose_name="تگ های جدید")
    schema1 = models.TextField(blank=True, null=True, verbose_name="اسکیما")
    schema2 = models.TextField(blank=True, null=True, verbose_name="اسکیما")

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = "دوره ها"
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments', verbose_name="دوره")
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies',
                                       verbose_name="والد")
    name = models.CharField(max_length=100, verbose_name='نام')
    phone = models.CharField(max_length=15, verbose_name='شماره همراه')
    email = models.EmailField(max_length=255, verbose_name='ایمیل')
    message = models.TextField(verbose_name='پیام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
        ordering = ('created_at',)

    def __str__(self):
        return f"{self.name} - {self.course.name}"


class CourseAttribute(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="دوره")
    key = models.CharField(max_length=100, verbose_name="نام ویژگی")
    value = models.CharField(max_length=255, verbose_name="مقدار ویژگی")

    def __str__(self):
        return f"{self.course.name} - {self.key}: {self.value}"

    class Meta:
        verbose_name = 'ویژگی'
        verbose_name_plural = "ویژگی ها"


class PageTags(models.Model):
    image = models.ImageField(upload_to="images/Tags", verbose_name='تصویر', blank=True, null=True)
    canonical = models.CharField(max_length=500, blank=True, null=True, verbose_name='Canonical')
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Description')
    locale = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:locale')
    type = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:type')
    title = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:title')
    descriptionOg = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:description')
    site_name = models.CharField(max_length=500, blank=True, null=True, verbose_name='Og:site_name')
    width = models.PositiveIntegerField(blank=True, null=True, verbose_name='Og:image:width')
    height = models.PositiveIntegerField(blank=True, null=True, verbose_name='Og:image:height')
    Index = (
        ('index', 'index'),
        ('noindex', 'noindex'),

    )
    Follow = (
        ('follow', 'follow'),
        ('nofollow', 'nofollow'),

    )
    index_noindex = models.CharField(max_length=150, choices=Index, default='index', blank=True, null=True)
    follow_nofollow = models.CharField(max_length=150, choices=Follow, default='follow', blank=True, null=True)
    twitter_title = models.CharField(max_length=500, blank=True, null=True, verbose_name='Twitter:title')
    twitter_description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Twitter:description')
    extratag = models.TextField(blank=True, null=True, verbose_name="تگ های جدید")
    schema1 = models.TextField(blank=True, null=True, verbose_name="اسکیما")
    schema2 = models.TextField(blank=True, null=True, verbose_name="اسکیما")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'تگ صفحه لیست دوره'
        verbose_name_plural = 'تگ های صفحه لیست دوره'

    def __str__(self):
        return "تگ صفحه لیست دوره"
