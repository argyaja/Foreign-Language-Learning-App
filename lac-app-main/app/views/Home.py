import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from app.models.CourseTaken import CourseTaken
from app.models.CourseTask import CourseTask
from app.models.CourseTakenProgress import CourseTakenProgress
from django.urls import reverse_lazy

@login_required(login_url=reverse_lazy('app:login'))
def home(request):

    current_user = request.user
    
    # Get all courses the user has taken
    courses_taken = CourseTaken.objects.filter(user=current_user)
    
    courses_progress = []
    
    for course_taken in courses_taken:
        course = course_taken.course
        course_id = course.id
        
        # Get all tasks for this course
        total_tasks = CourseTask.objects.filter(course=course).count()
        
        # Get the completed tasks for this course
        completed_tasks = CourseTakenProgress.objects.filter(user=current_user, course_taken=course_taken).values('course_task').distinct().count()
        
        # Calculate the progress
        progress = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0
        
        courses_progress.append({
            'course_id': course_id,
            'course': course,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'progress': progress,
        })
    
    
    return render(request, 'home.html', {'courses_progress': courses_progress})