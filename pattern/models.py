from django.utils import timezone

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class PatternCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')

    def __str__(self):
        return self.title


class Pattern(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.ManyToManyField(PatternCategory, related_name="articles", verbose_name='Category')
    slug = models.SlugField(unique=True, blank=True, verbose_name='Slug')
    body = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='images/patterns/')
    cover = models.FileField(upload_to='images/cover/patterns/', default=image)
    video = models.FileField(upload_to='videos/patterns/', blank=True, null=True)
    duration = models.CharField(max_length=200, default='Type...')
    alt = models.CharField(max_length=100, verbose_name='Alt', default='Alt')
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')
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


def __str__(self):
    return f"{self.title}"


def get_absolute_url(self):
    return reverse('pattern:pattern_detail', kwargs={'slug': self.slug})


class PatternPostViewLog(models.Model):
    pattern_post = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pattern_post.title} - {self.ip_address}"


class Comment(models.Model):
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE, related_name='comments')
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
    verbose_name = 'Pattern Page Tag'
    verbose_name_plural = 'Pattern Page Tags'


def __str__(self):
    return "Pattern Page Tags"
