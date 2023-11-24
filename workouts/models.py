from django.db import models

# Create your models here.

# Type model
class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Tipes'


# Intensity model
class Intensity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Intensities'

