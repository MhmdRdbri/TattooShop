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


admin.site.register(Pattern, PatternAdmin)
admin.site.register(PatternPostViewLog)
admin.site.register(Comment)
