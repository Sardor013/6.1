from django.shortcuts import render
from django.http import HttpResponse

def info(request):
    return HttpResponse("Vazifani muddatidan keyin topshirganim uchun uzur")

