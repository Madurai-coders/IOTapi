from django.conf.urls import url
from django.urls.conf import include
from .views import btnViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('data', btnViewset, basename='data')

urlpatterns = [
    url('', include(router.urls))
]