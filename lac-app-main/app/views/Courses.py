import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from app.forms.CourseForm import CourseForm
from app.models.Course import Course
from app.models.CourseTaken import CourseTaken
from django.urls import reverse_lazy

@login_required(login_url=reverse_lazy('app:login'))
def courses(request):
    sort = request.GET.get('sort', 'name_asc')
    
    if sort == 'name_desc':
        courses = Course.objects.all().order_by('-name')
    else:
        courses = Course.objects.all().order_by('name')
    user_courses = CourseTaken.objects.filter(user=request.user).values_list('course_id', flat=True)
    context = {
        'Courses': courses,
        'user_courses': user_courses,
    }
    return render(request, 'courses.html', context)

