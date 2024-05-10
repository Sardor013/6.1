from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("Samarqand qadimiy obidalar shahri")

# Create your views here.
