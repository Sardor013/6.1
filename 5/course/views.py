from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("Biz hozirda python dasturlash kursida ta'lim olyapmiz")
# Create your views here.
