import imp
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import Esp32camImg,IotChannelData
from .serializer import Esp32camImgSerializer,IotChannelDataSerializer
from django.core.files.storage import default_storage
import os

# Create your views here.

class IotChannelDataViewset(viewsets.ModelViewSet):
    queryset = IotChannelData.objects.all()
    serializer_class = IotChannelDataSerializer


class Esp32camImgViewset(viewsets.ModelViewSet):
    queryset = Esp32camImg.objects.all()
    serializer_class = Esp32camImgSerializer


    def perform_update(self, serializer):
        os.remove('media/images/esp32-cam.jpg')
        serializer.save()

