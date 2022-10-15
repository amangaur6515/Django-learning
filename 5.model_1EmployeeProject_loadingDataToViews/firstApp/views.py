from django.shortcuts import render
from firstApp.models import Employee
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'firstApp/index.html')
def empview(request):
    emp_list=Employee.objects.all()
    d={'emp_list':emp_list}
    return render(request,'firstApp/emp.html',context=d)
