from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field



class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')

    def __str__(self):
        return self.title

    def article_count(self):
        return self.articles.count()


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='admin', verbose_name='نویسنده')
    category = models.ManyToManyField(Category, related_name="articles", verbose_name='Category')
    title = models.CharField(max_length=100, verbose_name='Title')
    slug = models.SlugField(unique=True, blank=True, verbose_name='Slug')
    body = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to="images/articles", verbose_name='Image')
    alt = models.CharField(max_length=100, verbose_name='Alt')
    view_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')
    pub_date = models.DateField(default=timezone.datetime.now(), verbose_name='Publish Date')

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
        verbose_name='مقاله'
        verbose_name_plural='مقاله ها'
        ordering = ('-created',)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title}"


class BlogPostViewLog(models.Model):
    blog_post = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.blog_post.title} - {self.ip_address}"



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user.username} = {self.article.title}"

    class Meta:
        ordering = ('-created_at',)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    name = models.CharField(max_length=100, verbose_name='Name')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    email = models.EmailField(max_length=255, verbose_name='Email')
    message = models.TextField(verbose_name='Message')
    created = models.DateTimeField(default=timezone.now, verbose_name='Created')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('created',)

    def __str__(self):
        return f"Comment by {self.name} on {self.article.title}"