from django.contrib import admin
from firstApp.models import BangloreModel,PuneModel

# Register your models here.
class BangloreAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phoneNumber']

class PuneAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phoneNumber']

admin.site.register(BangloreModel,BangloreAdmin)
admin.site.register(PuneModel,PuneAdmin)