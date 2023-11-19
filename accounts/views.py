from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm


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


# User login view
def login_user(request):
    if request.method == 'POST':
        identifier = request.POST["username_or_email"]
        password = request.POST["password"]

        # Check if the identifier is an email
        if '@' in identifier:
            user = User.objects.filter(email=identifier).first()
        # Check if the identifier is a username
        elif '@' not in identifier:
            user = User.objects.filter(username=identifier).first()
        # Check if the identifier doesn't exist
        else:
            try:
                user = User.objects.get(username=identifier)
            except User.DoesNotExist:
                user = None

        if user:
            form = authenticate(
                request, username=identifier, password=password)
            if form is not None:
                login(request, form)
                messages.success(
                    request,
                    'Login successful.',
                    extra_tags='success'
                )
                # Redirect to home page after successful login
                return redirect('/')
            else:
                messages.error(
                    request,
                    'Invalid login credentials.',
                    extra_tags='danger'
                )
                # Redirect to login page if credentials are invalid
                return redirect('login_user')
        else:
            messages.error(
                request,
                'User does not exist.',
                extra_tags='danger'
            )
            # Redirect to registration page if user doesn't exist
            return redirect('register_user')
    else:
        return render(request, 'authentication/login.html', {})
    

# User logout view
def logout_user(request):
    logout(request)
    messages.success(
        request,
        'You have been logged out successfully. Come back soon!',
        extra_tags='info')
    return redirect('/')


# User profile view
@login_required
def user_profile(request):
    user = request.user
    context = {
        'user': user
        }
    return render(request, 'user_profile.html', context)
