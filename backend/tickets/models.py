from django.db import models
from events.models import EventModel
from users.models import AppUser

class TicketModel(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('cancelled', 'Cancelled'),
    )

    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    user = models.ForeignKey(AppUser, on_delete= models.CASCADE)
    qr_code = models.CharField(max_length=255, unique=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        constraints = [
            models.UniqueConstraint(fields=['event', 'user'], name='unique_event_user')
        ]

    def __str__(self):
        return f"Ticket for {self.event.title} ({self.user.username})"
