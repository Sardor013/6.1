from django.urls import path
from .views import about

urlpatterns = [
    path('url1', about, name='url1'),
]