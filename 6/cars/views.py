from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("GM avto uz")
    

# Create your views here.
