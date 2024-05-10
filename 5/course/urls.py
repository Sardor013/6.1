from django.urls import path
from .views import about

urlpatterns = [
    path('app_url', about, name='app_url'),
]