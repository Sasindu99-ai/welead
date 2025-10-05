from django.contrib import admin
from django.utils.html import format_html
from ..models import Event

__all__ = ['EventAdmin']


class EventLabelInline(admin.TabularInline):
    model = Event.labels.through
    extra = 1
    verbose_name = 'Event Label'
    verbose_name_plural = 'Event Labels'


class SponsorInline(admin.TabularInline):
    model = Event.sponsors.through
    extra = 1
    verbose_name = 'Sponsor'
    verbose_name_plural = 'Sponsors'


class AudienceInline(admin.TabularInline):
    model = Event.audiences.through
    extra = 1
    verbose_name = 'Audience'
    verbose_name_plural = 'Audiences'


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'coverImage', 'startDate', 'venue')
    list_display_links = ('name', )
    search_fields = ('name', 'shortDescription', 'description', 'venue')
    list_filter = ('startDate', 'labels', 'sponsors')
    ordering = ('-startDate', )
    readonly_fields = ('created_at', 'updated_at')
    inlines = [EventLabelInline, SponsorInline, AudienceInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'shortDescription', 'description', 'startDate', 'venue', 'cover')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'deleted_at'),
        }),
    )

    @staticmethod
    def coverImage(obj):
        if obj.cover:
            return format_html(f'<img src="{obj.cover.url}" style="max-height: 100px; max-width: 200px;" />')
        return "No Cover Image"
