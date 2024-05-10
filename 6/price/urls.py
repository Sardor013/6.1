from django.urls import path
from .views import narx

urlpatterns = [
    path('narx_url', narx, name='narx_url'),
]