from django.contrib import admin
from .models import *


class PatternImageInline(admin.TabularInline):
    model = PatternImage
    extra = 1


class PatternAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'created_at', 'updated_at')
    list_filter = ('category',)
    readonly_fields = ('view_count',)
    search_fields = ('name', 'title')
    prepopulated_fields = {'slug': ('name',)}

    inlines = [PatternImageInline]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pattern', 'name', 'email',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(Pattern, PatternAdmin)
admin.site.register(PatternPostViewLog)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PatternCategory)
admin.site.register(Tags)
