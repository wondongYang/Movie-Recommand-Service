from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    genre = models.ManyToManyField(Genre, related_name='movies')
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=50)
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)


class Actor(models.Model):
    movie = models.ManyToManyField(Movie, related_name='actors')
    name = models.CharField(max_length=50)