from django.db import models
from django.contrib.auth.models import User

from app.models.CourseTask import CourseTask
from app.models.Modul import Modul
from app.models.CourseTaken import CourseTaken


class CourseTakenProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_taken = models.ForeignKey(CourseTaken, on_delete=models.CASCADE)
    course_task = models.ForeignKey(CourseTask, on_delete=models.CASCADE)
    modul = models.ForeignKey(Modul, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, default='SEDANG DIKERJAKAN')