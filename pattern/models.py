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
    description = CKEditor5Field('Text', config_name='extends')
    video = models.FileField(upload_to='patterns/', blank=True, null=True)
    image = models.ImageField(upload_to='patterns/', blank=True, null=True)
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

    def __str__(self):
        return f"{self.title}"

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Pattern, self).save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})


class PatternImage(models.Model):
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='pattern_images/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.pattern.name}"


class PatternPostViewLog(models.Model):
    pattern_post = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pattern_post.title} - {self.ip_address}"