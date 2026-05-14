from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from app.models.Course import Course
from app.models.CourseTask import CourseTask
from app.models.Modul import Modul
from app.models.TaskQuestionAudio import TaskQuestionAudio

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

    # Menentukan apakah pengguna saat ini adalah admin
    is_admin = request.user.is_superuser

    # Check if there are any modules or TaskQuestionAudio objects
    has_modules = modul.exists()
    has_task_question_audio = TaskQuestionAudio.objects.filter(modul__in=modul).exists()

    context = {
        'course': course,
        'task': task,
        'next_task': next_task,
        'previous_task': previous_task,
        'modul': modul,
        'is_admin': is_admin,
        'has_modules': has_modules,
        'has_task_question_audio': has_task_question_audio,
    }
    
    return render(request, 'Modul_detail.html', context)