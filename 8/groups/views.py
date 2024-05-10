from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("Jami bolib 74 ta guruhlar mavjud")

# Create your views here.
