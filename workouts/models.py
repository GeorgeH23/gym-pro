from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Type model
class Type(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Tipes'


# Intensity model
class Intensity(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Intensities'


# Workout model
class Workout(models.Model):
    title = models.CharField(max_length=100, blank=False)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    description = models.TextField()
    intensity = models.ForeignKey(Intensity, on_delete=models.CASCADE)
    burned = models.CharField(max_length=100, blank=False)
    image_url = CloudinaryField('image', default='default')
    slug = models.SlugField(max_length=100, unique=True)

    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='workout_details'
    )
    likes = models.ManyToManyField(
        User,
        related_name='liked_workouts',
        blank=True
    )
    liked_by_user = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title}'
