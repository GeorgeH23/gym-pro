from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# User Profile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField(
        'Profile Picture', default='profile_picture')

    def __str__(self):
        username = getattr(self.user, 'username', 'NoUsername')
        return 'Profile: {}'.format(username)
