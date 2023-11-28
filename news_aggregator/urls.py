# news_aggregator/urls.py

from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    # Add other URLs as needed
]