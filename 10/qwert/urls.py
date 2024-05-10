from django.urls import path
from .views import func

urlpatterns = [
    path('func', func, name='func'),
]