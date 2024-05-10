from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Shahrimizga xush kelibsiz")

# Create your views here.
