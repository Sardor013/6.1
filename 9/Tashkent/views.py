from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("Toshkent Uzbekistanning poytaxti")

# Create your views here.
