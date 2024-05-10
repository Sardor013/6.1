from django.urls import path
from .views import credit

urlpatterns = [
    path('credit_url', credit, name='credit_url'),
]