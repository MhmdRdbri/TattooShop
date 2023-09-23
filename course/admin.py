from django.contrib import admin
from .models import *
from .forms import CourseAttributeForm


class CourseAttributeInline(admin.TabularInline):
    model = CourseAttribute
    form = CourseAttributeForm
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [CourseAttributeInline]

    fieldsets = (
        (None, {
            'fields': ('name', 'media', 'alt', 'body', 'slug')
        }),
        (
            "Seo",
            {
                "classes": ["collapse"],
                "fields": ["pagetitle", "description", "canonical", "localeOg", "typeOg", "titleOg", "descriptionOg",
                           "site_name", "widthOg", "heightOg"],
            },
        ),
    )


class TagsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Tags, TagsAdmin)
