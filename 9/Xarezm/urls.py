from django.urls import path
from .views import about

urlpatterns = [
    path('url3', about, name='url3'),
]