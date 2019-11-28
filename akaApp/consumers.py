from channels.db import database_sync_to_async
from channels.consumer import AsyncConsumer
import asyncio
from .models import *
from .serializers import *
import json
from django.contrib.auth import get_user_model

User = get_user_model()



class CommentConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print(event)
        await self.send({
            'type': 'websocket.accept'
        })
        # await self.receive
        self.city = self.scope['user'].city.name

        print(self.city, self.scope['user'])

        await self.channel_layer.group_add(
            self.city,
            self.channel_name
        )

    async def websocket_receive(self, event):
        data = json.loads(event.get('text'))
        print(data)
   
        await self.create_order(data)

        new_order = {
            'customer': {
                'id': User.objects.get(pk=data['cs_id']).pk,
                'phone': User.objects.get(pk=data['cs_id']).phone
            },
            'a_name': data['a_name'],
            'b_name': data['b_name']
        }
        await self.channel_layer.group_send(
            self.city,
            {
                'type': 'show_order',
                'text': json.dumps(new_order)
            }
        )

    async def show_order(self, event):
        await self.send({
                'type': 'websocket.send',
                'text': event['text']
            })

    @database_sync_to_async
    def create_order(self, data):
        u = User.objects.get(pk=data['cs_id'])
        # cr = User.objects.get(pk=data['cr_id'])
        Order.objects.create(
            customer=u,
            a_name=data['a_name'],
            b_name=data['b_name']
        )