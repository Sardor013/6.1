from django.urls import path
from .views import about

urlpatterns = [
    path('about_url', about, name='about_url'),
]