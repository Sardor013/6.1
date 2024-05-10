from django.shortcuts import render
from django.http import HttpResponse

def func(request):
    return HttpResponse("WWW.")

# Create your views here.
