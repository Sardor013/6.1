from django.urls import path
from .views import about

urlpatterns = [
    path('url', about, name='url'),
]