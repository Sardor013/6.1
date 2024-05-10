from django.urls import path
from .views import about

urlpatterns = [
    path('ab_url', about, name='ab_url'),
]