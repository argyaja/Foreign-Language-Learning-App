import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from app.models.Course import Course
from app.models.CourseTask import CourseTask
from app.models.Modul import Modul
from django.urls import reverse_lazy

@login_required(login_url=reverse_lazy('app:login'))
def Modul_detail(request, course_id, task_id):
    course = get_object_or_404(Course, id=course_id)
    task = get_object_or_404(CourseTask, id=task_id, course=course)
    
    # Mengambil level dari task saat ini
    current_level = task.level

    # Mengambil task dengan level yang lebih rendah dan lebih tinggi
    next_task = CourseTask.objects.filter(course=course, level__gt=current_level).order_by('level').first()
    previous_task = CourseTask.objects.filter(course=course, level__lt=current_level).order_by('-level').first()

    modul = Modul.objects.filter(course_task=task)

    context = {
        'course': course,
        'task': task,
        'next_task': next_task,
        'previous_task': previous_task,
        'modul': modul,
    }
    print (context)

    return render(request, 'Modul_detail.html', context)