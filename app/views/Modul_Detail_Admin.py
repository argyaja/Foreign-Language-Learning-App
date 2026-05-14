from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from app.models.Modul import Modul
from app.models.CourseTask import CourseTask
from app.forms.ModulForm import ModulForm
from django.urls import reverse_lazy
from django.contrib import messages

@login_required(login_url=reverse_lazy('app:login'))
def modul_create(request, course_id, task_id):
    task = get_object_or_404(CourseTask, pk=task_id)
    if request.method == 'POST':
        form = ModulForm(request.POST)
        if form.is_valid():
            modul = form.save(commit=False)
            modul.course_task = task
            modul.save()
            messages.success(request, 'Modul created successfully!')
            return redirect('app:Modul_detail', course_id=course_id, task_id=task_id)
    else:
        form = ModulForm()
    return render(request, 'modul_detail_form_admin.html', {'form': form, 'task': task})

@login_required(login_url=reverse_lazy('app:login'))
def modul_edit(request, course_id, task_id, modul_id):
    modul = get_object_or_404(Modul, pk=modul_id, course_task__pk=task_id)
    if request.method == 'POST':
        form = ModulForm(request.POST, instance=modul)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modul edited successfully!')
            return redirect('app:Modul_detail', course_id=course_id, task_id=task_id)
    else:
        form = ModulForm(instance=modul)
    return render(request, 'modul_detail_form_admin.html', {'form': form, 'task': modul.course_task})

@login_required(login_url=reverse_lazy('app:login'))
def modul_update(request, course_id, task_id, modul_id):
    modul = get_object_or_404(Modul, pk=modul_id, course_task__pk=task_id)
    if request.method == 'POST':
        form = ModulForm(request.POST, instance=modul)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modul updated successfully!')
            return redirect('app:Modul_detail', course_id=course_id, task_id=task_id)
    else:
        form = ModulForm(instance=modul)
    return render(request, 'modul_detail_form_admin.html', {'form': form})

@login_required(login_url=reverse_lazy('app:login'))
def modul_delete(request, course_id, task_id, modul_id):
    modul = get_object_or_404(Modul, pk=modul_id)
    if request.method == "POST":
        modul.delete()
        messages.success(request, 'Modul deleted successfully!')
        return redirect('app:Modul_detail', course_id=course_id, task_id=task_id)
    return render(request, 'confirm_delete.html', {'modul': modul})