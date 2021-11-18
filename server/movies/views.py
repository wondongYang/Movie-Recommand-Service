from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.views.decorators.http import require_safe

from .models import Movie

from .serializers import MovieListSerializer, MovieSerializer

# Create your views here.
@require_safe
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@require_safe
def movie_detail(reqeust, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@require_safe
def movie_recommended(request):
    pass