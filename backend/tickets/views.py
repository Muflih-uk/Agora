from rest_framework import viewsets, permissions
from .serializers import TicketSerializer
from .models import TicketModel
import uuid

class TicketViewSet(viewsets.ModelViewSet):

    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TicketModel.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        qr_code = str(uuid.uuid4())
        serializer.save(user=self.request.user, qr_code= qr_code)


