import imp
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import btn,turfImages
from .serializer import Btnserializer,TurfImageSerializer
from django.core.files.storage import default_storage
import os

# Create your views here.

class btnViewset(viewsets.ModelViewSet):

    serializer_class = Btnserializer

    def get_queryset(self):
        button = btn.objects.all()
        return button

    # def retrieve(self, request, *args, **kwargs):
    #     get_button = btn.objects.filter()
    #     serializer = btnserializer(get_button, many=True)
    #     return Response(serializer.data)


class TurfImageViewset(viewsets.ModelViewSet):
    queryset = turfImages.objects.all()
    serializer_class = TurfImageSerializer

    def perform_update(self, serializer):
        os.remove('media/images/esp32-cam.jpg')
        serializer.save()

