from rest_framework import viewsets, permissions
from .models import EventModel
from .serializers import EventSerializer
from django_filters.rest_framework import DjangoFilterBackend

class EventViewSet(viewsets.ModelViewSet):

    queryset = EventModel.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date_time', 'category', 'location_name']

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)