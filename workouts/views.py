from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Workout

# Create your views here.


def get_home_page(request):
    return render(request, 'workouts/home.html')


# My Workouts
@login_required
def user_page(request):
    user = request.user

    user_workouts = Workout.objects.filter(user_id=user.id)
    context = {
        'user': user,
        'workouts': user_workouts,
    }
    return render(request, 'workouts/user_page.html', context=context)
