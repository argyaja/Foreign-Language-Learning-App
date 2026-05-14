import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from app.models.CourseTaken import CourseTaken
from django.db.models import Sum
from django.urls import reverse_lazy

@login_required(login_url=reverse_lazy('app:login'))
def leaderboards(request):
    user = request.user

    # Get the leaderboard data
    leaderboard_data = (CourseTaken.objects
                        .values('user__username')
                        .annotate(total_points=Sum('point'))
                        .order_by('-total_points')[:10])

    # Get the current user's points
    user_points = (CourseTaken.objects
                   .filter(user=user)
                   .aggregate(total_points=Sum('point'))
                   ['total_points'] or 0)

    return render(request, 'leaderboards.html', {
        'leaderboard_data': leaderboard_data,
        'user_points': user_points
    })