from django.urls import path
from .views import about

urlpatterns = [
    path('url2', about, name='url2'),
]