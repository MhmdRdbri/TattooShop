from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام دسته بندی')
    slug = models.CharField(max_length=120, unique=True, default='slug', verbose_name='نامک')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')

    def __str__(self):
        return self.title

    def article_count(self):
        return self.articles.count()

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ('-created',)


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='admin', verbose_name='نویسنده')
    category = models.ManyToManyField(Category, related_name="articles", verbose_name='دسته بندی')
    title = models.CharField(max_length=100, verbose_name="عنوان")
    slug = models.SlugField(unique=True, verbose_name='نامک')
    body = CKEditor5Field('متن', config_name='extends')
    image = models.ImageField(upload_to="images/articles", verbose_name='تصویر')
    alt = models.CharField(max_length=100, verbose_name='جایگزین تصویر')
    view_count = models.PositiveIntegerField(default=0, verbose_name='تعداد بازدید')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')

    # tags
    pagetitle = models.CharField(max_length=500, blank=True, null=True, verbose_name='Title')
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Description')
    canonical = models.CharField(max_length=500, blank=True, null=True,
                                 verbose_name='Canonical(default set on current page)')
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
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse('blog:articles_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title}"


class BlogPostViewLog(models.Model):
    blog_post = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    ip_address = models.GenericIPAddressField(verbose_name='آی پی کاربر')
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.blog_post.title} - {self.ip_address}"

    class Meta:
        verbose_name = 'بازدید'
        verbose_name_plural = 'بازدید ها'
        ordering = ('-updated',)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name='کاربر')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes', verbose_name='مقاله')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} = {self.article.title}"

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'
        ordering = ('-created_at',)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله')
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies', verbose_name='کامنت والد')
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
        return f"{self.name} - {self.article.title}"


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
    index_noindex = models.CharField(max_length=150, choices=Index, default='index')
    follow_nofollow = models.CharField(max_length=150, choices=Follow, default='follow')
    twitter_title = models.CharField(max_length=500, blank=True, null=True, verbose_name='Twitter:title')
    twitter_description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Twitter:description')
    extratag = models.TextField(blank=True, null=True, verbose_name="تگ های جدید")
    schema1 = models.TextField(blank=True, null=True, verbose_name="اسکیما")
    schema2 = models.TextField(blank=True, null=True, verbose_name="اسکیما")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'تگ صفحه لیست بلاگ'
        verbose_name_plural = 'تگ های صفحه لیست بلاگ'

    def __str__(self):
        return "تگ های صفحه لیست بلاگ"
