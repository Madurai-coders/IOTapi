from django.conf.urls import url
from django.urls.conf import include
from .views import btnViewset,TurfImageViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('data', btnViewset, basename='data')
router.register(r'turf_image',TurfImageViewset, basename='add_image_for_admin')

urlpatterns = [
    url('', include(router.urls))
]