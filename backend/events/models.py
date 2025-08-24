from django.db import models
from users.models import AppUser
from datetime import datetime


# Create your models here.

class EventModel(models.Model):
    CATEGORY_CHOICES = (
        ('Workshop', 'Workshop'),
        ('Sports', 'Sports'),
        ('Hackathon', 'Hackathon'),
        ('Art', 'Art'),
        ('Conference', 'Conference'),
        ('Other', 'Other'),
    )

    title = models.CharField(max_length=255)
    description = models.CharField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    location_name = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    ticket_limit = models.IntegerField()
    host = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_time']
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title


