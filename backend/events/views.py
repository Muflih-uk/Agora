from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from .models import EventModel
from .serializers import EventSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class EventViewSet(viewsets.ModelViewSet):

    queryset = EventModel.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date_time', 'category', 'location_name']

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)

    @action(detail=False, methods=['get'], url_path='category/(?P<category_name>[^/.]+)')
    def get_by_category(self, request, category_name=None):
        events = self.get_queryset().filter(category__iexact=category_name)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)