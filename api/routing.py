from django.urls import re_path
from . import consumer

websocket_urlpatterns = [
    # re_path(r'ws/iot/$', consumer.IotConsumer.as_asgi()),
    re_path(r'ws/iot_change/$', consumer.ModelConsumerObserver.as_asgi()),
    re_path(r'ws/sensordata/$', consumer.SensorConsumerObserver.as_asgi()),

]