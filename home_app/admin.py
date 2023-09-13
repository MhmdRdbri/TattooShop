from django.contrib import admin
from django.forms import BaseInlineFormSet
from .models import *


class ReadOnlyMessageAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Message', 'created_at')
    readonly_fields = ('Name', 'Email', 'Phone', 'Message', 'created_at')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(Message, ReadOnlyMessageAdmin)
admin.site.register(Pattern)
