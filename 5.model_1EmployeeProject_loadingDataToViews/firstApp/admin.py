from django.contrib import admin
from firstApp.models import Employee

#this class will help display table information on 
#admin interface
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddr'] 
#register this model admin class


# Register your models here.
#admin.site.register(Employee)
admin.site.register(Employee,EmployeeAdmin)
