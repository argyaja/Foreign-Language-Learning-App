from django.db import models
from django.contrib.auth.models import User

from app.models.Course import Course

class CourseTask(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    level = models.IntegerField()
    
    def __str__(self):
        return f"{self.course} - {self.name} - {self.level}"