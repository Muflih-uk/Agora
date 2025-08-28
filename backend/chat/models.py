from django.db import models
from events.models import EventModel
from users.models import AppUser

class Message(models.Model):
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE, related_name="messages")
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']