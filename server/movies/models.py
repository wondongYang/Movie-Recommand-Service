from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Movie(models.Model):
    genre_ids = models.ManyToManyField(Genre, related_name='movies')
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=50)
    overview = models.TextField()
    poster_path = models.CharField(max_length=500, blank=True, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

    def __str__(self):
        return f'{self.title}'