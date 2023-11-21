from django.shortcuts import render
from django.http import HttpResponse
from demoapp1.models import *
# Create your views here.
def home(request):
    return render(request,'base.html')
def index(request):
    return HttpResponse("Welcome")