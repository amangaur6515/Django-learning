from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    d={'msg':date}
    return render(request,'testApp/wish.html' ,context=d)
