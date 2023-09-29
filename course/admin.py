from django.contrib import admin
from django import forms

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
                           "site_name", "widthOg", "heightOg", "extratag", "schema1", "schema2"],
            },
        ),
    )


class PageTagsAdminForm(forms.ModelForm):
    class Meta:
        model = PageTags
        fields = ['description', 'locale', 'type', 'title', 'descriptionOg', 'site_name', 'width', 'height', 'extratag',
                  'schema1', 'schema2']


class PageTagsAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        if obj:  # If an object already exists, allow editing only
            kwargs['form'] = PageTagsAdminForm
        return super().get_form(request, obj, **kwargs)

    def has_add_permission(self, request):
        # Check if there is already an existing product
        return not PageTags.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Disallow product deletion
        return False

    def has_change_permission(self, request, obj=None):
        return True


class CommentAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'email',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(Comment, CommentAdmin)
admin.site.register(PageTags, PageTagsAdmin)
