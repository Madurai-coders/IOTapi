from rest_framework import serializers
from api.models import IotChannelData,Esp32camImg
from django.contrib.auth.models import User



class IotChannelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IotChannelData
        fields = ['id','name','value']


class Esp32camImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Esp32camImg
        fields = '__all__' 

    
