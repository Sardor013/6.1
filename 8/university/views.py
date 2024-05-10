from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("PDP University")

# Create your views here.
