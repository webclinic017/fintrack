from django.contrib import admin

from fintrack_be.admin.linkify import linkify
from fintrack_be.models import Industry


class IndustryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': (
            'name',
            'sector'
        )}),
    )

    list_display = ('name', linkify(field_name='sector'),)
    list_filter = ('sector',)
    search_fields = ('name', 'sector')
    ordering = ('name',)


admin.site.register(Industry, IndustryAdmin)
