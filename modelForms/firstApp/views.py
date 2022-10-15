from django.shortcuts import render
from firstApp import forms
# Create your views here.

def studentView(request):
    form=forms.StudentForm()
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('data inserted successfully')

    return render(request,'firstApp/index.html',{'form':form})
    

