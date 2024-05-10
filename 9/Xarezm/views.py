from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("Ichanqala bilan mashhur shahar")

# Create your views here.
