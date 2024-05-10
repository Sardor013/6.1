from django.urls import path
from .views import info

urlpatterns = [
    path('app2_url', info, name='app2_url'),
]