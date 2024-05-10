from django.urls import path
from .views import fayl

urlpatterns = [
    path('app2_url', fayl, name='app2_url'),
]