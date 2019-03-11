from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("rango says hello <a href='/rango/about'>about</a>")

def about(request):
    return HttpResponse("This is the about page <a href='/rango/'>index</a")
