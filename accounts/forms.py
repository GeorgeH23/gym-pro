from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from cloudinary.forms import CloudinaryFileField


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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError(
                'This email has already been used.')
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        # Password complexity validation
        if not any(char.isupper() for char in password1):
            raise forms.ValidationError(
                'Password must contain at least one uppercase letter.')
        if not any(char.islower() for char in password1):
            raise forms.ValidationError(
                'Password must contain at least one lowercase letter.')
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError(
                'Password must contain at least one digit.')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        # Override the default form fields
        for field_name in self.fields:
            if 'password' in field_name:
                self.fields[field_name].widget.attrs[
                    'autocomplete'] = 'new-password'
            else:
                self.fields[field_name].widget.attrs['autocomplete'] = 'off'


# Update User Profile Form
class UpdateProfileForm(UserChangeForm):
    email = forms.EmailField(
        label='Email:',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address'}
        ),
        required=False,
        help_text='',
    )

    profile_image = CloudinaryFileField(
        label='Change Profile Image',
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control form-label'}
        ),
        required=False,
    )

    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-label',
            'placeholder': 'New Password',
            'title': 'Min 7 chars, at least 1 uppercase, 1 lowercase, 1 digit.'}
        ),
        required=False,
    )

    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-label',
            'placeholder': 'Confirm New Password'}
        ),
        required=False,
    )

    class Meta:
        model = User
        fields = ('email', 'profile_image', 'new_password1', 'new_password2',)


# Contact Form
class ContactForm(forms.Form):
    fullName = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Full Name (required)',
            'id': 'fullName'}
        ),
        required=True,
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email (required)',
            'id': 'email'}
        ),
        required=True,
    )
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Write your message (required)',
            'id': 'message'}
        ),
    )
