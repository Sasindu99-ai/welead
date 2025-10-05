from django.contrib import admin

__all__ = ['AudienceAdmin']


class AudienceAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', 'description')
    ordering = ('-created_at', )
    list_display_links = ('name', )
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'deleted_at'),
        }),
    )
