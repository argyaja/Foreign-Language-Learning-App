import os
from app.models.Course import Course
from app.forms.CourseForm import CourseForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User

def admin_courses(request):   
    Courses = Course.objects.all()    
    return render(request, 'admin-courses.html', {'Courses': Courses})

def admin_add_course(request):
    users = User.objects.all()
    flag_icon_choices = Course.FLAG_ICON_CHOICES
    lang_choices = [(lang, lang) for lang in Course.LANGUAGE_CHOICES]

    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Course added successfully!')
                return redirect('app:admin-courses')
            except Exception as e:
                messages.error(request, f'Error adding course: {e}')
        else:
            messages.error(request, 'Form is not valid. Please correct the errors.')
    else:
        form = CourseForm()
    context = {
        'form': form,
        'users': users,
        'flag_icon_choices' : flag_icon_choices,
        'lang': lang_choices,
    }
    return render(request, 'admin-course-add.html', context)
    

def admin_edit_course(request, id):
    course_object = get_object_or_404(Course, pk=id)
    users = User.objects.all()
    flag_icon_choices = Course.FLAG_ICON_CHOICES
    lang_choices = [(lang, lang) for lang in Course.LANGUAGE_CHOICES]

    context = {
        'course': course_object,
        'users': users,
        'flag_icon_choices' : flag_icon_choices,
        'lang': lang_choices,
        
    }
    
    return render(request, 'admin-course-edit.html', context)


def admin_update_course(request, id):
    course_object = get_object_or_404(Course, pk=id)
    old_image_path = course_object.image.path if course_object.image else None
    users = User.objects.all()
    flag_icon_choices = Course.FLAG_ICON_CHOICES
    lang_choices = [(lang, lang) for lang in Course.LANGUAGE_CHOICES]
     
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course_object)
        if form.is_valid():
            if 'image' in request.FILES:
                if old_image_path and os.path.isfile(old_image_path):
                    os.remove(old_image_path)
            form.save()
            messages.success(request, 'Course updated successfully!')
            return redirect('app:admin-edit-course', id=id)
        else:
            messages.error(request, 'Form is not valid. Please correct the errors.')
    else:
        form = CourseForm(instance=course_object)
    
    context = {
        'form': form,
        'course': course_object,
        'users': users,
        'flag_icon_choices' : flag_icon_choices,
        'lang': lang_choices,
    }
    return render(request, 'admin-course-edit.html', context)


def admin_delete_course(request, id):
    course_object = get_object_or_404(Course, pk=id)
    if course_object.image:
        image_path = os.path.join('/media/', course_object.image.path)
        if os.path.isfile(image_path):
            os.remove(image_path)
    course_object.delete()
    messages.success(request, 'Course deleted successfully!')
    return redirect("/administrator/courses") 