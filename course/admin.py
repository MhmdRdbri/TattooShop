from django.contrib import admin
from .models import *

from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Dynamic Attributes', {
            'fields': ('dynamic_attributes',),
            'classes': ('collapse',),
        }),
    )
