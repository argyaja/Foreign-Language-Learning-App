import os
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from app.models.Quest import Quest
from app.models.CourseTaken import CourseTaken
from django.db.models import Sum
from django.urls import reverse_lazy

# Courses
@login_required(login_url=reverse_lazy('app:login'))
def quest(request):
    user = request.user

    # Mengambil total poin pengguna yang sedang login
    user_points = (CourseTaken.objects
                   .filter(user=user)
                   .aggregate(total_points=Sum('point'))
                   ['total_points'] or 0)
    quests = Quest.objects.filter(user=user, status='BELUM DIKERJAKAN')

    return render(request, 'quest.html', {'quests': quests, 'user_points': user_points})
