from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('app:login')