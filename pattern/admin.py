from django.contrib import admin
from .models import *


class PatternAdmin(admin.ModelAdmin):
    readonly_fields = ('view_count',)


admin.site.register(Pattern, PatternAdmin)
admin.site.register(PatternPostViewLog)
