from django.contrib import admin
from .models import *


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Dynamic Attributes', {
            'fields': ('dynamic_attributes',),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Customize the form widget for dynamic_attributes to be a textarea
        form.base_fields['dynamic_attributes'].widget.attrs['widget'] = 'textarea'
        return form
