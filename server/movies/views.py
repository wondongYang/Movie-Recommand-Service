from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Movie

from .serializers import MovieListSerializer, MovieSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@permission_classes([AllowAny])
@api_view(['GET'])
def movie_recommended(request):
    pass