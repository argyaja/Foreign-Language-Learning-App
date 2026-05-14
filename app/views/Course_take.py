from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from app.models.Course import Course
from app.models.CourseTaken import CourseTaken
from django.contrib import messages
from django.urls import reverse_lazy

@login_required(login_url=reverse_lazy('app:login'))
def take_course(request, id):
    course = get_object_or_404(Course, pk=id)
    course_taken, created = CourseTaken.objects.get_or_create(
        user=request.user,
        course=course,
        defaults={'point': 0}  # Menambahkan nilai default untuk field point
    )
    if created:
        messages.success(request, f'You have successfully taken the course "{course.name}".')
    else:
        messages.info(request, f'You have already taken the course "{course.name}".')
    return redirect('app:home')
