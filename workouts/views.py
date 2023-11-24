from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.contrib import messages
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

    def post(self, request):
        form = WorkoutForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            workout = form.save(commit=False)
            workout.user = user
            workout.save()

            messages.success(
                request,
                f'Workout "{workout.title}" successfully added!',
                extra_tags='success'
            )
            return redirect('user_page')
        else:
            messages.error(
                request,
                'There was an error with the form. \
                    Please correct the errors and try again.',
                extra_tags='danger'
            )

        tipes = Type.objects.all()
        intensities = Intensity.objects.all()

        context = {
            'form': form,
            'tipes': tipes,
            'intensities': intensities,
        }
        return render(request, 'workouts/add_workout.html', context)
