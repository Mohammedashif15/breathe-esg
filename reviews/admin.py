from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'emission',
        'analyst_name',
        'status',
        'reviewed_at'
    )

    list_filter = (
        'status',
        'reviewed_at'
    )

    search_fields = (
        'analyst_name',
        'status'
    )

    ordering = (
        '-reviewed_at',
    )