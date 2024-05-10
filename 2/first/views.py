from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("Bu Django proyekt haqida ma'lumot.")


        
    
