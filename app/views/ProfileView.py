from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.forms.ProfileForm import ProfileForm
from app.models.Profile import Profile
from app.models.Profile import Language

@login_required
def profile_view(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=user_profile)
    
    if form.is_valid():
        form.save()
        return redirect('app:profile')

    context = {
        'user': request.user,
        'user_details': user_profile,
        'form': form,
    }
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=user_profile)
    
    if form.is_valid():
        form.save()
        print(f"Language saved: {user_profile.language}")
        return redirect('app:profile')

    languages = Language.objects.all()

    context = {
        'form': form,
        'user': request.user,
        'user_details': user_profile,
        'languages': languages,
    }
    return render(request, 'profileEdit.html', context)
