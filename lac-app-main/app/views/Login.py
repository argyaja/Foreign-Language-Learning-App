from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

def login(request):
    # Jika pengguna sudah login, redirect ke halaman index
    if request.user.is_authenticated:
        return redirect('app:index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            next_url = request.POST.get('next')
            if next_url:
                return HttpResponseRedirect(next_url)
            else:
                return redirect('app:index')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        if not request.user.is_authenticated and request.GET.get('next'):
            messages.warning(request, "You need to login first to access that page.")
    
    next_url = request.GET.get('next', '')
    return render(request, 'login.html')
