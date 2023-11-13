from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistrationForm
from .models import UserProfile


# User registration view
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        form.is_valid()
        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        form = authenticate(username=username, password=password)
        login(request, user)
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'authentication/register.html', context)
