from django.db import models
from django.contrib.auth.models import User

from app.models.CourseTask import CourseTask
    
class Modul(models.Model):
    course_task = models.ForeignKey(CourseTask, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.course_task} - {self.name}"