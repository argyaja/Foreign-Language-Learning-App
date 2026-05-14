from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

@login_required
def confirm_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        user = authenticate(username=request.user.username, password=current_password)
        if user is not None:
            return redirect('app:change_password')
        else:
            messages.error(request, 'Incorrect password. Please try again.')
    return render(request, 'passwordConfirm.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password == confirm_password:
            user = request.user
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # Keep the user logged in
            messages.success(request, 'Your password has been updated successfully!')
            return redirect('app:profile')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')
    return render(request, 'passwordChange.html')
