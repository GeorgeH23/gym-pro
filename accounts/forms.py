from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# User Registration Form
class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username (required)',
            'title': 'Enter your username'},
        ),
        required=True,
        help_text='',
    )

    email = forms.EmailField(
        max_length=120,
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address (required)',
            'title': 'Enter a valid email address.'},
        ),
        required=True,
        help_text='',
    )

    password1 = forms.CharField(
        min_length=7,
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password (required)',
            'title': 'Min 7 chars, at least 1 uppercase, 1 lowercase, 1 digit.'
            },
        ),
        required=True,
        help_text=''
    )

    password2 = forms.CharField(
        min_length=7,
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password (required)',
            'title': 'Passwords must match'},
        ),
        required=True,
        help_text='',
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', )
