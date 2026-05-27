from django.contrib import admin
from .models import (
    DataSource,
    RawRecord
)


@admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'source_type',
        'uploaded_file',
        'uploaded_at'
    )

    list_filter = (
        'source_type',
        'uploaded_at'
    )

    search_fields = (
        'source_type',
    )

    ordering = (
        '-uploaded_at',
    )


@admin.register(RawRecord)
class RawRecordAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'source',
        'created_at'
    )

    list_filter = (
        'created_at',
    )

    search_fields = (
        'source__source_type',
    )

    ordering = (
        '-created_at',
    )