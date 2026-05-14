import os
import random
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from app.models.Course import Course
from app.models.CourseTask import CourseTask
from app.models.Modul import Modul
from app.models.TaskQuestionFill import TaskQuestionFill
from app.models.TaskQuestionVideo import TaskQuestionVideo
from app.models.TaskQuestionAudio import TaskQuestionAudio
from app.models.TaskQuestionMCQ import TaskQuestionMCQ
from app.models.CourseTakenProgress import CourseTakenProgress
from app.models.CourseTaken import CourseTaken
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.db.models import Sum
from random import shuffle
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse_lazy

# Courses
@login_required(login_url=reverse_lazy('app:login'))
def quiz(request, course_id, task_id):
    course = get_object_or_404(Course, id=course_id)
    task = get_object_or_404(CourseTask, id=task_id, course=course)

    tasks_audio = list(TaskQuestionAudio.objects.filter(modul__course_task=task))
    tasks_mcq = list(TaskQuestionMCQ.objects.filter(modul__course_task=task))
    tasks_video = list(TaskQuestionVideo.objects.filter(modul__course_task=task))

    # Gabungkan tugas secara selang-seling
    tasks = []
    max_len = max(len(tasks_audio), len(tasks_mcq), len(tasks_video))
    for i in range(max_len):
        if i < len(tasks_audio):
            tasks_audio[i].type_name = 'TaskQuestionAudio'
            tasks.append(tasks_audio[i])
        if i < len(tasks_mcq):
            tasks_mcq[i].type_name = 'TaskQuestionMCQ'
            tasks.append(tasks_mcq[i])
        if i < len(tasks_video):
            tasks_video[i].type_name = 'TaskQuestionVideo'
            tasks.append(tasks_video[i])

    paginator = Paginator(tasks, 1)  # Satu pertanyaan per halaman
    page_number = request.GET.get('page')
    try:
        tasks_page = paginator.page(page_number)
    except PageNotAnInteger:
        tasks_page = paginator.page(1)
    except EmptyPage:
        tasks_page = paginator.page(paginator.num_pages)

    total_tasks = len(tasks)
    
    context = {
        'course': course,
        'task': task,
        'tasks_page': tasks_page,
        'total_tasks': total_tasks,
    }
    # return render(request, 'quiz.html', context)

    if request.method == "POST" and 'finish' in request.POST:
        course_taken, created = CourseTaken.objects.get_or_create(user=request.user, course=course)
        course_taken.point += 10
        course_taken.save()
        return redirect('app:Modul_detail', course_id=course.id, task_id=task.id)

    return render(request, 'quiz.html', context)
