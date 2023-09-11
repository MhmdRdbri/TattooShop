from django.contrib import admin
from .models import *


class FlatPageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:80; height:80px"/>'.format(obj.image.url))

    list_display = ('title', 'image_tag', 'author')
    fieldsets = [
        (
            "Article",
            {
                "fields": ["author", "title", "category", "slug", "image", "alt", "pub_date"],
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


admin.site.register(Article, FlatPageAdmin)
admin.site.register(Category)
admin.site.register(Like)
