from rest_framework import serializers
from .models import EventModel

class EventSerializer(serializers.ModelSerializer):
    host = serializers.ReadOnlyField(source='host.username')

    class Meta:
        model = EventModel
        fields = [
            'id', 'title', 'description', 'category', 'location_name',
            'date_time', 'ticket_limit', 'host', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']