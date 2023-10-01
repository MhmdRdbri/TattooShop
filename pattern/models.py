from django.utils import timezone

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class PatternCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام دسته بندی')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ('-created',)


class Pattern(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام')
    title = models.CharField(max_length=255, verbose_name='عنوان')
    category = models.ManyToManyField(PatternCategory, related_name="articles", verbose_name='دسته بندی')
    slug = models.SlugField(unique=True, blank=True, verbose_name='نامک')
    body = CKEditor5Field('متن', config_name='extends')
    image = models.ImageField(upload_to='images/patterns/', verbose_name='تصویر')
    cover = models.FileField(upload_to='images/cover/patterns/', default=image, verbose_name='کاور وبدئو')
    video = models.FileField(upload_to='videos/patterns/', blank=True, null=True, verbose_name='وبدئو')
    duration = models.CharField(max_length=200, default='Type...', blank=True, null=True, verbose_name='مدت زمان ویدئو')
    alt = models.CharField(max_length=100, verbose_name='Alt', default='جایگزین تصویر')
    view_count = models.PositiveIntegerField(default=0, verbose_name='بازدید')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی')
    # tags
    pagetitle = models.CharField(max_length=500, blank=True, null=True, verbose_name='Title')
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Description')
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
        verbose_name = 'طرح پیشنهادی'
        verbose_name_plural = 'طرح های پیشنهادی'
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('pattern:pattern_detail', kwargs={'slug': self.slug})


class PatternPostViewLog(models.Model):
    pattern_post = models.ForeignKey(Pattern, on_delete=models.CASCADE, verbose_name='طرح')
    ip_address = models.GenericIPAddressField(verbose_name='آی پی کاربر')
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pattern_post.title} - {self.ip_address}"

    class Meta:
        verbose_name = 'بازدید'
        verbose_name_plural = 'بازدید ها'


class Comment(models.Model):
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE, related_name='comments', verbose_name='طرج')
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies',
                                       verbose_name='والد')
    name = models.CharField(max_length=100, verbose_name='نام')
    phone = models.CharField(max_length=15, verbose_name='شماره همراه')
    email = models.EmailField(max_length=255, verbose_name='ایمیل')
    message = models.TextField(verbose_name='پیام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
        ordering = ('-created_at',)

    def __str__(self):
        return f"Comment by {self.name} on {self.pattern.title}"


class Tags(models.Model):
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
        verbose_name = 'تگ صفحه لیست طرح پیشنهادی'
        verbose_name_plural = 'تگ های صفحه لیست طرح پیشنهادی'

    def __str__(self):
        return "تگ صفحه لیست طرح پیشنهادی"
