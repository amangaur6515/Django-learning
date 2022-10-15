from django.contrib import admin
from firstApp.models import Movies
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['name','rating']

admin.site.register(Movies,MovieAdmin)

