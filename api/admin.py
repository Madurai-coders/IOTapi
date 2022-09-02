from re import I
from django.contrib import admin
from api.models import  IotChannelData,Esp32camImg

# Register your models here.
admin.site.register(IotChannelData)
admin.site.register(Esp32camImg)