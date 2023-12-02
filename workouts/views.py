from django.http import HttpResponseBadRequest
from django.urls import reverse
from django.views import View
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Workout, Type, Intensity
from .forms import WorkoutForm
import pdb 
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


# Workout Detail View
class WorkoutDetail(LoginRequiredMixin, View):

    def get(self, request, slug):
        queryset = Workout.objects.all()
        workout = get_object_or_404(queryset, slug=slug)

        # like button
        liked_by_user = False
        if workout.likes.filter(id=request.user.id).exists():
            liked_by_user = True

        context = {
            'workout': workout,
            'liked_by_user': liked_by_user,
             }
        return render(request, 'workouts/detail_workout.html', context=context)


# Like Workout View (from the 'workout_detail' view)
@login_required
def like_workout_detail(request, slug):
    if request.method == 'POST' and request.user.is_authenticated:
        workout = get_object_or_404(Workout, slug=slug)

        # Check the like status
        liked_by_user = workout.likes.filter(id=request.user.id).exists()

        if liked_by_user:
            workout.likes.remove(request.user)
        else:
            workout.likes.add(request.user)

        return redirect('detail_workout', slug=slug)


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
            workout.user_id = user
            slug_count = Workout.objects.filter(title=workout.title).count() + 1
            workout.slug = slugify(workout.title + str(slug_count))
            workout.save()

            messages.success(
                request,
                (f'Workout "{workout.title}" successfully added!'),
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


# Workout Edit (Update) View
class WorkoutUpdateView(LoginRequiredMixin, View):
    def get(self, request, slug):
        if not slug:
            return HttpResponseBadRequest("Invalid workout slug")

        workout = get_object_or_404(Workout, slug=slug)
        form = WorkoutForm(instance=workout)
        tipes = Type.objects.all()
        intensities = Intensity.objects.all()
        workout.description = workout.description.strip()
        context = {
            'workout': workout,
            'form': form,
            'tipes': tipes,
            'intensities': intensities,
        }
        return render(request, 'workouts/edit_workout.html', context)

    def post(self, request, slug):
        if not slug:
            return HttpResponseBadRequest("Invalid workout slug")

        workout = get_object_or_404(Workout, slug=slug)
        tipes = Type.objects.all()
        intensities = Intensity.objects.all()
        form = WorkoutForm(request.POST, request.FILES, instance=workout)

        if form.is_valid():
            # Save the form
            form.save()

            # Success message
            messages.success(
                request,
                (f'Workout "{workout.title}" successfully updated!'),
                extra_tags='success')
            return redirect('user_page')

        context = {
            'workout': workout,
            'form': form,
            'tipes': tipes,
            'intensities': intensities,
        }
        return render(request, 'workouts/edit_workout.html', context)
    

# Delete Workout View
class WorkoutDeleteView(LoginRequiredMixin, View):
    def get(self, request, slug):
        workout = get_object_or_404(Workout, slug=slug)
        workout.delete()

        messages.success(
            request,
            (f'Workout "{workout.title}" successfully deleted!'),
            extra_tags='success'
            )

        return redirect('user_page')


def workout_delete_confirmation(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)

    if request.method == 'POST':
        workout.delete()
        return redirect('user_page')

    return render(request, 'workouts/delete_workout.html', {'workout': workout})

# https://docs.djangoproject.com/en/4.0/topics/db/queries/#complex-lookups-with-q-objects
# Find Workout View
@login_required
def search_workout(request):

    query = request.GET.get('q')
    if query:
        workouts = Workout.objects.filter(
            Q(title__icontains=query) | Q(type__name__icontains=query) |
            Q(intensity__name__icontains=query))
    else:
        workouts = Workout.objects.all()

    context = {
        'workouts': workouts,
    }
    return render(request, 'workouts/search_workout.html', context=context)
