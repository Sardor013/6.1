from django.shortcuts import render
from django.http import HttpResponse

def music(request):
    return HttpResponse("Musiqangizni tanlab eshtishingiz mumkin faqat proekt toliq bitgandan keyin")
    

# Create your views here.
