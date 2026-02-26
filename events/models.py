from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Registration(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('professional', 'Working Professional'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Registered')
    
    # Additional registration questions
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    degree_or_position = models.CharField(max_length=100)
    organization = models.CharField(max_length=100, blank=True)
    experience_years = models.IntegerField(null=True, blank=True)
    expectations = models.TextField(blank=True, help_text="What do you hope to gain from this event?")
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
