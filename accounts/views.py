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

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request,
                ('Registration successful. Welcome!'),
                extra_tags='success'
            )
            return redirect('/')
        else:
            messages.error(
                request,
                ('Registration failed. Please correct the errors.'),
                extra_tags='danger'
            )
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'authentication/register.html', context)


def login_user(request):
    if request.method == 'POST':
        identifier = request.POST["username_or_email"]
        password = request.POST["password"]

    else:
        return render(request, 'authentication/login.html', {})
