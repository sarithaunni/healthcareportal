from django.contrib import admin
from .models import Appoinment
# Register your models here.
class Appoinmentadmin(admin.ModelAdmin):
    list_display=['user','doctor','appoinmentdate','status']
    list_filter=['user','doctor','appoinmentdate','status']

admin.site.register(Appoinment,Appoinmentadmin)