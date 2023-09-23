from django.contrib import admin
from .models import *


class FlatPageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:80; height:80px"/>'.format(obj.image.url))

    list_display = ('title', 'image_tag', 'author', 'view_count')
    fieldsets = [
        (
            "Article",
            {
                "fields": ["author", "title", "category", "slug", "image", "alt"],
            },
        ),
        (
            "Editor",
            {
                "fields": ["body"],
            },
        ),
        (
            "Seo",
            {
                "classes": ["collapse"],
                "fields": ["pagetitle", "description", "canonical", "localeOg", "typeOg", "titleOg", "descriptionOg",
                           "site_name", "widthOg", "heightOg"],
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
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Article, FlatPageAdmin)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Comment, CommentAdmin)
