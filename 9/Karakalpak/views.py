from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("Uzbekistan hududidagi boshqa bir respublika")

# Create your views here.
