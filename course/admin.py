from django.contrib import admin
from .models import *


class CourseAttributeInline(admin.TabularInline):
    model = Course.attributes.through
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )

    inlines = [CourseAttributeInline]


@admin.register(CourseAttribute)
class CourseAttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
