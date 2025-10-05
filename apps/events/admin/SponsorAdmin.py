from django.contrib import admin
from django.utils.html import format_html

__all__ = ['SponsorAdmin']


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'logoPreview', 'website')
    list_display_links = ('name',)
    ordering = ('-created_at', )
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'logo', 'website', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'deleted_at'),
        }),
    )

    @staticmethod
    def logoPreview(obj):
        if obj.cover:
            return format_html(f'<img src="{obj.cover.url}" style="max-height: 100px; max-width: 200px;" />')
        return "No Logo"
