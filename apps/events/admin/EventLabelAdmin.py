from django.contrib import admin
from django.utils.html import format_html

__all__ = ['EventLabelAdmin']

class EventLabelAdmin(admin.ModelAdmin):
    list_display = ('label', )
    list_filter = ('created_at', )
    list_display_links = ('label',)
    search_fields = ('name',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'color')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'deleted_at'),
        }),
    )

    @staticmethod
    def label(obj):
        color = f'rgba({int(obj.color[1:3], 16)}, {int(obj.color[3:5], 16)}, {int(obj.color[5:7], 16)}, 1)'
        bgColor = f'rgba({int(obj.color[1:3], 16)//2 + 5}, {int(obj.color[3:5], 16)//2 + 5}, {int(obj.color[5:7], 16)//2 + 5}, 0.18)'
        borderColor = f'rgba({int(obj.color[1:3], 16)}, {int(obj.color[3:5], 16)}, {int(obj.color[5:7], 16)}, 0.8)'
        return format_html(f"""
        <span style="display: inline-block; padding: 5px 10px; border-radius: 17px;
            background-color: {bgColor}; border: 1px solid {borderColor}; 
            color: {color}; font-weight: bold;">
                {obj.name}
        </span>
        """)
