from app.models.Profile import Profile

def user_context_processor(request):
    user_profile = None
    if request.user.is_authenticated:
        user_profile, created = Profile.objects.get_or_create(user=request.user)

    return {
        'user': request.user,
        'user_details': user_profile,
    }
