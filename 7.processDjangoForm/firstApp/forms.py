from django import forms
#for validation
from django.core import validators
def nameValidator(name):
    if name[0]!='a' or name[0]!='A':
        raise forms.ValidationError('name must start with A')

class StudentForm(forms.Form):
    First_Name=forms.CharField(validators=[nameValidator])
    Last_Name=forms.CharField()
    Email=forms.EmailField()
    Phone_Number=forms.IntegerField()
    Password=forms.CharField(widget=forms.PasswordInput)
    Re_type_password=forms.CharField(widget=forms.PasswordInput)
    Feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(5)])

    def clean(self):
        cleaned_data=super().clean()
        pwd=cleaned_data['Password']
        rpwd=cleaned_data['Re_type_password']
        if pwd!=rpwd:
            raise forms.ValidationError('Password not matched')