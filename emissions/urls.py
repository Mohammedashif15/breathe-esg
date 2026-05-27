from django.urls import path
from .views import (
    get_emissions,
    suspicious_records,
    update_review
)

urlpatterns = [

    path(
        'list/',
        get_emissions,
        name='emission-list'
    ),

    path(
        'suspicious/',
        suspicious_records,
        name='suspicious-records'
    ),

    path(
        'review/',
        update_review,
        name='update-review'
    ),
]