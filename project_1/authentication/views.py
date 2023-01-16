from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Learn Everyday & Discover a world of new possibilities</h1>")
def about(request):
    return HttpResponse("<h2>Power Learn Project is an impact organization whose goal is to drive transformative change for youth in Africa by powering them with relevant technology capacity through provision of quality and decentralized tech training.</h2>")
