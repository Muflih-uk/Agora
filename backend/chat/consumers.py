import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_group_name = None
        self.event_id = None

    async def connect(self):
        self.event_id = self.scope['url_route']['kwargs']['event_id']
        self.room_group_name = f'chat_{self.event_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        from .models import Message
        from events.models import EventModel
        from users.models import AppUser

        data = json.loads(text_data)
        message = data['message']
        user_id = data['user_id']

        saved_message = await self.save_message(self.event_id, user_id, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': saved_message.message,
                'user': saved_message.user.username,
                'timestamp': str(saved_message.timestamp)
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def save_message(self, event_id, user_id, message):
        from .models import Message
        from events.models import EventModel
        from users.models import AppUser

        event = EventModel.objects.get(id=event_id)
        user = AppUser.objects.get(id=user_id)
        return Message.objects.create(event=event, user=user, message=message)
