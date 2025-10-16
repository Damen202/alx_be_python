from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

PRIORITY_CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
]

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
]

class User(AbstractUser):
    pass

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='Pending')
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def mark_complete(self):
        self.status = 'Completed'
        self.completed_at = timezone.now()
        self.save()

    def mark_incomplete(self):
        self.status = 'Pending'
        self.completed_at = None
        self.save()

    def save(self, *args, **kwargs):
        if self.due_date < timezone.now():
            raise ValueError("Due date must be in the future.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.status})"
