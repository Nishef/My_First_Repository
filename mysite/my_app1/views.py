from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Transo") 

# Create your views here.
