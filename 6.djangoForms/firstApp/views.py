from django.shortcuts import render
from . import forms
# Create your views here.
def studentRegistrationView(request):
    #create form object
    form=forms.studentRegistration()
    return render(request,'firstApp/index.html',context={'form':form})
