
from cgitb import lookup
from random import randint
from time import sleep
from api.models import btn
from .serializer import Btnserializer
import json
from djangochannelsrestframework.mixins import ListModelMixin,RetrieveModelMixin,PatchModelMixin,UpdateModelMixin,CreateModelMixin,DeleteModelMixin
from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer

from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.decorators import action

from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.consumers import AsyncAPIConsumer


class IotConsumer(ListModelMixin,
        RetrieveModelMixin,
        PatchModelMixin,
        UpdateModelMixin,
        CreateModelMixin,
        DeleteModelMixin,GenericAsyncAPIConsumer):
    queryset = btn.objects.all()
    serializer_class = Btnserializer


class ModelConsumerObserver(AsyncAPIConsumer,AsyncWebsocketConsumer):
    async def accept(self, **kwargs):
        await super().accept(** kwargs)
        await self.model_change.subscribe()
   
    @model_observer(btn)
    async def model_change(self, message, action=None, **kwargs):
        await self.send_json(message)

    ''' If you want the data serialized instead of pk '''
    @model_change.serializer
    def model_serialize(self, instance, action, **kwargs):
        return Btnserializer(instance).data

        

    


class SensorConsumerObserver(AsyncAPIConsumer,AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = 'kaamil'
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        dict_type={
                    'type': 'chat_message',
                }
        res = { **dict_type,**text_data_json,}
        # res=json.dumps(res)

       
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            res
        )

    # Receive message from room group
    async def chat_message(self, event):
        print(event)
    # Send message to WebSocket
        await self.send(text_data=json.dumps(event))
            
       