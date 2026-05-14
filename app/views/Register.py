import os
from django.conf import settings

from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login

from app.forms.CreateUserForm import CreateUserForm

## Register
def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')
    

    context = {'form':form}
    
    return render(request, 'register.html', context)