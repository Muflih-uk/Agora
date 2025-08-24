from rest_framework import serializers
from .models import TicketModel
class TicketSerializer(serializers.ModelSerializer):

    event_title = serializers.ReadOnlyField(source='event.title')
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = TicketModel
        fields = ['id', 'event', 'user', 'event_title', 'user_username', 'qr_code', 'status', 'created_at']
        read_only_fields = ['id', 'user', 'qr_code', 'created_at']