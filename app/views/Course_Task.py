import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from app.forms.CourseTaskForm import CourseTaskForm
from app.models.Course import Course
from app.models.CourseTask import CourseTask
from django.urls import reverse_lazy


@login_required(login_url=reverse_lazy('app:login'))
def course_tasks(request, course_id):
    tasks = CourseTask.objects.filter(course_id=course_id)
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_task_list.html', {'tasks': tasks, 'course': course})

def course_task_list_add(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseTaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.course = course
            task.save()
            messages.success(request, 'Task added successfully!')
            return redirect('app:course_tasks', course_id=course_id)
    else:
        form = CourseTaskForm()
    
    return render(request, 'course_task_list_add.html', {'form': form, 'course': course})

def course_task_create(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    if request.method == 'POST':
        form = CourseTaskForm(request.POST, request.FILES)
        if form.is_valid():
            course_task = form.save(commit=False)
            course_task.course = course
            course_task.save()
            return redirect('app:course_tasks', course_id=course_id)
    else:
        form = CourseTaskForm(initial={'course': course})

    return render(request, 'course_task_add.html', {'form': form, 'course': course})

def course_task_update(request, pk):
    task = get_object_or_404(CourseTask, pk=pk)
    course_id = task.course.id 
    if request.method == 'POST':
        form = CourseTaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('app:course_tasks', course_id=course_id)
        else:
            print(form.errors)
    else:
        form = CourseTaskForm(instance=task)

    return render(request, 'course_task_edit.html', {'form': form, 'task': task})

def course_task_delete(request, pk):
    task = get_object_or_404(CourseTask, pk=pk)
    course_id = task.course.id 
    task.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('app:course_tasks', course_id=course_id)
