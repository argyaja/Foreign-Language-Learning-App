from django.db import models
from django.contrib.auth.models import User

from app.models.Modul import Modul

class TaskQuestionFill(models.Model):
    modul= models.ForeignKey(Modul, on_delete=models.CASCADE)
    question_text = models.TextField()