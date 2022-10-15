from django import forms

class studentRegistration(forms.Form):
    Name=forms.CharField()
    Rollno=forms.IntegerField()
