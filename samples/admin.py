from django.contrib import admin
from .models import *
from django import forms


class TagsAdminForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['image', 'description', 'locale', 'type', 'title', 'descriptionOg', 'site_name', 'width',
                  'height',
                  'index_noindex', 'follow_nofollow', 'twitter_title', 'twitter_description', 'extratag', 'schema1',
                  'schema2']


class TagsAdmin(admin.ModelAdmin):
    list_display = (
        'description', 'title')

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


admin.site.register(Samples)
admin.site.register(SamplesCategory)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Comment)
