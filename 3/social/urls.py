from django.urls import path
from .views import music

urlpatterns = [
    path('app_url', music, name='app_url'),
]