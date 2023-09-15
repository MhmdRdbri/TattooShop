from django.contrib import admin
from .models import Course, CourseAttribute
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
            'fields': ('name', 'media','alt','description','slug')
        }),
    )
