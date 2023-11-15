from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.models import *

def home(request):
    # d={'name':'Alex','age':20}
    d=student.objects.all()
    return render(request,'home.html',{'d':d})

def index(request):
    return HttpResponse("hello welcome to this page")