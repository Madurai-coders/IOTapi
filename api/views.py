from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import btn
from .serializer import Btnserializer


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