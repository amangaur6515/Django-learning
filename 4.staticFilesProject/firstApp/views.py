from django.shortcuts import render



# Create your views here.

def welcome(request):
    
    return render(request,'firstApp/welcome.html')


def profile(request):
    return render(request,'firstApp/profile.html')
