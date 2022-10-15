from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def wish(request):
    s='<h1>Hello worlld!!</h1>'
    return HttpResponse(s)
    
