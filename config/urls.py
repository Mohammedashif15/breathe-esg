from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "Breathe ESG Backend Running Successfully"
    )


urlpatterns = [

    path(
        '',
        home
    ),

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        'api/ingestion/',
        include('ingestion.urls')
    ),

    path(
        'api/emissions/',
        include('emissions.urls')
    ),

    path(
        'api/reviews/',
        include('reviews.urls')
    ),
]