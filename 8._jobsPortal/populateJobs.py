#sync this file with models.py
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsPortal.settings')
import django
django.setup()


#import models and faker
from firstApp.models import *
from faker import Faker
from random import *

#faker object
fake=Faker()
#generate random
def generatePhoneNumber():
    d1=randint(7,9)
    num=""+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)

#main function  to populate
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Software Engineer','Business Analyst','Software Tester'))
        feligibility=fake.random_element(elements=('Btech.','Mtech.','MCA','PHD'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=generatePhoneNumber()
        #important

        banglore_record=BangloreModel.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phoneNumber=fphonenumber
        )
        pune_record=PuneModel.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phoneNumber=fphonenumber
        )


populate(25)

