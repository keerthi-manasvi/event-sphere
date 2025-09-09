from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class User(AbstractUser):
    isOrganizer = models.BooleanField(default=False)

class Event(models.Model):
    title = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    date = models.DateField(default=datetime.date.today)
    Img = models.URLField(blank=True, null=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, default='General')

    def __str__(self):
        return self.title 
    
class Feedback(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='feedbacks')
    name = models.CharField(max_length=100)
    feedback = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
