from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Movie, Genre

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


# DB에 접근해야 하는 작업은 Vue보다 Django에서 처리하는 것이 맞을 것 같습니다.
# 예를 들어 영화 장르별 인기 영화 10개를 이렇게 뽑겠습니다. 
# -> vue에서 보여지는 편의성을 위해 3개로 수정했습니다!
@api_view(['GET'])
@permission_classes([AllowAny])
def genre_top_list(request, genre_name):
    genre_id = get_object_or_404(Genre, name=genre_name.title())
    movies = get_list_or_404(Movie, genre_ids__in=[genre_id])[:3]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# 위처럼 출력 형식에 따라 (리스트를 줄 건지? 무엇을 포함할 것인지? 하나만 줄 건지?) serializer를 선택하되,
# serializer 안에 들어갈 내용을 바꿔서 집어넣으면 됩니다.