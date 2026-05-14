from django.db import models
from django.contrib.auth.models import User

from app.models.Course import Course

class CourseTaken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    point = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.course} - {self.point}"