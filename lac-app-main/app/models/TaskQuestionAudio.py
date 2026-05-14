from django.db import models
from django.contrib.auth.models import User
from app.models.Modul import Modul

class TaskQuestionAudio(models.Model):
    modul = models.ForeignKey(Modul, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.modul} - {self.question_text}"