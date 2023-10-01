from django import forms
from django.contrib import admin
from .models import *


class FlatPageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:80; height:80px"/>'.format(obj.image.url))

    list_display = ('title', 'image_tag', 'author', 'view_count')
    fieldsets = [
        (
            "مقاله",
            {
                "fields": ["author", "title", "category", "slug", "image", "alt"],
            },
        ),
        (
            "ویرایشگر متن",
            {
                "fields": ["body"],
            },
        ),
        (
            "سئو",
            {
                "classes": ["collapse"],
                "fields": ["pagetitle", "description", "localeOg", "typeOg", "titleOg", "descriptionOg",
                           "site_name", "widthOg", "heightOg", 'index_noindex', 'follow_nofollow', 'twitter_title',
                           'twitter_description', "extratag",
                           "schema1",
                           "schema2"],
            },
        ),
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'name', 'email',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


class TagsAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'descriptionOg', 'index_noindex',
        'follow_nofollow')

    def get_form(self, request, obj=None, **kwargs):
        if obj:  # If an object already exists, allow editing only
            kwargs['form'] = TagsAdminForm
        return super().get_form(request, obj, **kwargs)

    def has_add_permission(self, request):
        # Check if there is already an existing product
        return not Tags.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Disallow product deletion
        return False


class TagsAdminForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['image', 'canonical', 'description', 'locale', 'type', 'title', 'descriptionOg', 'site_name', 'width',
                  'height',
                  'index_noindex', 'follow_nofollow', 'twitter_title', 'twitter_description', 'extratag', 'schema1',
                  'schema2']


admin.site.register(Article, FlatPageAdmin)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Comment, CommentAdmin)
