from django.urls import path
from .views import get_about

urlpatterns = [
    path('app2_url', get_about, name='app2_url'),
]