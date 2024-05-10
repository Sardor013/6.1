from django.urls import path
from .views import about

urlpatterns = [
    path('url4', about, name='url4'),
]