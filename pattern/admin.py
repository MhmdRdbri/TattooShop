from django.contrib import admin
from .models import *
from django import forms


class PatternAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'created_at', 'updated_at')
    list_filter = ('category',)
    readonly_fields = ('view_count',)
    search_fields = ('name', 'title')
    prepopulated_fields = {'slug': ('name',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pattern', 'name', 'email',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


class TagsAdminForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['image', 'canonical', 'description', 'locale', 'type', 'title', 'descriptionOg', 'site_name', 'width',
                  'height',
                  'index_noindex', 'follow_nofollow', 'twitter_title', 'twitter_description', 'extratag', 'schema1',
                  'schema2']


class TagsAdmin(admin.ModelAdmin):

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

    def has_change_permission(self, request, obj=None):
        return True


admin.site.register(Pattern, PatternAdmin)
admin.site.register(PatternPostViewLog)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PatternCategory)
admin.site.register(Tags, TagsAdmin)
