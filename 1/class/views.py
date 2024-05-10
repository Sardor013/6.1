from django.shortcuts import render
from django.http import HttpResponse

def get_about(request):
    return HttpResponse("Python!!!")

# Create your views here.
