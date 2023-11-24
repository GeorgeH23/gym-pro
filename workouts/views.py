from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Workout, Type, Intensity
from .forms import WorkoutForm

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


# Workout Add View
class AddWorkoutView(LoginRequiredMixin, View):
    def get(self, request):
        form = WorkoutForm()
        tipes = Type.objects.all()
        intensities = Intensity.objects.all()

        context = {
            'form': form,
            'tipes': tipes,
            'intensities': intensities,
        }
        return render(request, 'workouts/add_workout.html', context)

