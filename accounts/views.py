from django.shortcuts import render, redirect
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from accounts.models import UserProfile
from .forms import ContactForm, RegistrationForm, UpdateProfileForm


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
                request, username=user.username, password=password)
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


# Update Profile View
@login_required
def update_profile(request):
    if UserProfile.objects.filter(user=request.user).exists():
        user_profile = UserProfile.objects.get(user=request.user)
    else:
        # If the user's profile doesn't exist, create a new one
        user_profile = UserProfile(user=request.user)
        user_profile.save()

    if request.method == 'POST':
        form = UpdateProfileForm(
            request.POST,
            instance=request.user
        )
        if form.is_valid():
            # model instance is only in memory, not saved in DB (yet)
            user = form.save(commit=False)
            # Check if the user entered a new password
            new_password = form.cleaned_data.get('new_password1')
            new_password_confirm = form.cleaned_data.get('new_password2')

            if new_password:
                # Validate the new password
                try:
                    validate_password(new_password, user=request.user)
                except ValidationError as errors:
                    for error in errors.error_list:
                        form.add_error('new_password1', error)
                    return render(request, 'user_update.html', {'form': form})

                # Check if new_password1 and new_password2 match
                if new_password != new_password_confirm:
                    form.add_error(
                        'new_password2',
                        'The two password fields didn\'t match.'
                    )
                    return render(request, 'user_update.html', {'form': form})

                # Handle password update logic here
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
            
            # Verify if user changed his email
            new_email = form.cleaned_data.get('email')
            if new_email and new_email != user.email:
                try:
                    # Validate the new email format
                    validate_email(new_email)
                except ValidationError:
                    form.add_error(
                        'email',
                        'The format of the email is invalid.'
                    )
                    return render(request, 'user_update.html', {'form': form})

                # Check if the new email address is unique
                if User.objects.filter(email=new_email).exclude(
                        username=user.username
                    ).exists():
                    form.add_error(
                        'email',
                        'This email address is already in use.'
                    )
                    return render(request, 'user_update.html', {'form': form})

                # Update the email address
                user.email = new_email
                user.save()
            
            user.save()
            messages.success(request, (
                'Your profile was successfully updated!'),
                extra_tags='success')
            return redirect('user_profile')
    else:
        form = UpdateProfileForm(instance=request.user)

    return render(request, 'user_update.html', {'form': form})


@login_required
def delete_account(request):
    if request.method == 'POST':
        # Delete user and log out
        request.user.delete()
        return redirect('/')

    return render(request, 'user_profile.html', {'user': request.user})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your message was sent successfully.')
        else:
            messages.error(
                request,
                'There was an error sending your message. Please try again.'
            )
        return redirect('contact')
    # Pre-fill the email field if the user is authenticated
    if request.user.is_authenticated:
        initial_data = {'email': request.user.email}
        form = ContactForm(initial=initial_data)
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
