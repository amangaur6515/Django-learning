from django.shortcuts import render
from firstApp import forms
from firstApp.models import *
# Create your views here.
def Welcome(request):
    return render(request,'firstApp/index.html')

def AddMovie(request):
    form=forms.MovieForm()
    if request.method=='POST':
        form=forms.MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('added')


    return render(request,'firstApp/addMovie.html',{'form':form})

def ListMovie(request):
    movieList=Movies.objects.order_by('rating')
    d={'movieList':movieList}
    return render(request,'firstApp/listMovie.html',context=d)
