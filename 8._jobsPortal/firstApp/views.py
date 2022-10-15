from django.shortcuts import render
from firstApp.models import *
# Create your views here.
def welcome(request):
    return render(request,'firstApp/index.html')

def bangloreJobs(request):
    jobsList=BangloreModel.objects.order_by('date')
    d={'jobsList':jobsList}
    return render(request,'firstApp/banglore.html',context=d)

