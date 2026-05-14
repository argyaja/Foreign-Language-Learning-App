from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
    name = models.CharField(max_length=255) 
    email = models.EmailField()
    query = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Question from {self.name}"
