import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Movie(models.Model):
    name = models.CharField(max_length=255) 
    release_date = models.DateField(null=True)
    rating = models.DecimalField(null=True, max_digits=2, decimal_places=1)
    description = models.TextField(null=True)
    poster = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT, "cinematrix"), null=True)

    class MovieType(models.TextChoices):
        MOVIE = 'mov', _('Movie')
        TV = 'tvs', _('TV Series')

    class MovieCertification(models.TextChoices):
        UNRESTRICTED = 'u', _('U')
        ABOVE12 = 'ua', _('U/A')
        ADULT_A = 'a', _('A')
        ADULT_R = 'r', _('R')
        SPECIAL = 's', _('S')
        NOT_AVAILABLE = 'na', _('N/A')

    type = models.CharField(max_length=7, choices=MovieType.choices, default=MovieType.MOVIE)   
    certification = models.CharField(max_length=3, choices=MovieCertification.choices, default=MovieCertification.NOT_AVAILABLE)  

    def __str__(self):
        return self.name

class User(AbstractUser):
    last_login = None
    favourite_movie = models.ManyToManyField(Movie)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.username}'

class Language(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    language = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.language} - {self.movie.name}'

class Genre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.genre} - {self.movie.name}'

class StreamingSite(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    site = models.CharField(max_length=2048)

    def __str__(self):
        return f'{self.site} - {self.movie.name}'
