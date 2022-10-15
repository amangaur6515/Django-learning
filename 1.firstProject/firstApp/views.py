from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def welcome(request):
    
    s="Hello good morning!! "
    return HttpResponse(s)

