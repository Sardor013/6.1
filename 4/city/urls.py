from django.urls import path
from .views import welcome

urlpatterns = [
    path('app_url/', welcome, name='app_url'),
]