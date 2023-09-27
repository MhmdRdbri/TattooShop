from django.contrib import admin
from .models import *
from django import forms


class TagsAdmin(admin.ModelAdmin):
    list_display = (
    'description', 'locale', 'type', 'title', 'descriptionOg', 'site_name', 'width', 'height', 'extratag')

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
        fields = ['description', 'locale', 'type', 'title', 'descriptionOg', 'site_name', 'width', 'height', 'extratag']


admin.site.register(Samples)
admin.site.register(SamplesCategory)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Comment)
