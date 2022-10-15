from django.shortcuts import render
from . import forms
# Create your views here.
def StudentView(request):
    form=forms.StudentForm()
    #if request is coming for submitting process the form data
    if request.method=='POST':
        #create form object again
        form=forms.StudentForm(request.POST)
        #if valid
        if form.is_valid():
            #printing data
            #all data is present in cleaned_data dictionary
            print('Form Submitted!')
            print('First_Name:',form.cleaned_data['First_Name'])
            print('Last_Name:',form.cleaned_data['Last_Name'])
            print("EmaiL:",form.cleaned_data['Email'])
            print("Feedback",form.cleaned_data['Feedback'])
            return render(request,'firstApp/thankyou.html')


    return render(request,'firstApp/index.html',{'form':form})
