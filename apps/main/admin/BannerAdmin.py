from django.contrib import admin
from django.utils.html import format_html

__all__ = ['BannerAdmin']


class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'imagePreview', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('page', )
    ordering = ('-created_at',)
    list_per_page = 20
    date_hierarchy = 'created_at'
    actions = ['mark_as_active']
    readonly_fields = ('imagePreview', 'created_at', 'updated_at', 'deleted_at')
    fieldsets = (
        (None, {
            'fields': ('image', 'title', 'description', 'primaryButtonText', 'primaryButtonLink',
                       'secondaryButtonText', 'secondaryButtonLink', 'order', 'page', 'isActive')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'deleted_at'),
        }),
    )

    def mark_as_active(self, request, queryset):
        queryset.update(isActive=True)
        self.message_user(request, "Selected banners marked as active.")

    @staticmethod
    def imagePreview(obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="100" />')
        return "No Image"
