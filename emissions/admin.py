from django.contrib import admin
from .models import EmissionRecord


@admin.register(EmissionRecord)
class EmissionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'source_type',
        'activity_type',
        'scope',
        'quantity',
        'co2e',
        'is_suspicious',
        'review_status',
        'locked_for_audit'
    )

    list_filter = (
        'scope',
        'review_status',
        'is_suspicious'
    )

    search_fields = (
        'activity_type',
        'source_type'
    )