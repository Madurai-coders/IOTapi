from django.conf.urls import url
from django.urls.conf import include
from .views import IotChannelDataViewset,Esp32camImgViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('iot_data', IotChannelDataViewset, basename='iot_data')
router.register('esp32_img',Esp32camImgViewset, basename='esp32_img')

urlpatterns = [
    url('', include(router.urls))
]