from django.shortcuts import render

from django.shortcuts import HttpResponse
# Create your views here.

def home(request):
    return  HttpResponse ("our application is data for home page")

def about(request):
    return HttpResponse ("This is About us page")