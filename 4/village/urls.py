from django.urls import path
from .views import vill

urlpatterns = [
    path('app2_url', vill, name='app2_url'),
]