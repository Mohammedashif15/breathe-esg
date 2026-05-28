from django.urls import path
from .views import (
    ReviewCreateView,
    ReviewActionView,
    ReviewListView
)

urlpatterns = [

    path(
        'create/',
        ReviewCreateView.as_view(),
        name='review-create'
    ),

    path(
        'action/',
        ReviewActionView.as_view(),
        name='review-action'
    ),

    path(
        'list/',
        ReviewListView.as_view(),
        name='review-list'
    ),
]