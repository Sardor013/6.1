from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("2024-yil uchun qabul boshlanmoqda")
# Create your views here.
