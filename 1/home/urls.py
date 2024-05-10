from django.urls import path
from .views import get_info


urlpatterns = [
    path('app_url', get_info, name='app_url'),
  
]