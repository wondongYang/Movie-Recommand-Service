import datetime

from django.http.response import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model

from community.models import Review

from .models import Movie, Genre

from .serializers import MovieListSerializer, MovieSerializer, SimpleGenreSeriliazer

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# 각각 몇개 들고 올까요?
N = 16
@api_view(['GET'])
@permission_classes([AllowAny])
def latest_movie_list(request):
    # poster_path가 있고 오늘 이전에 개봉하는 영화의 개봉일 내림차순 각각 5개
    movies = get_list_or_404(Movie.objects.exclude(poster_path=None).exclude(overview='').order_by('-release_date'), release_date__lte=datetime.date.today())[:N]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def review_desc_movie_list(request):
    # Movie에 달린 Review를 세어서 (reviews__count) 갯수 역순으로 5개
    movies = Movie.objects.annotate(Count('like_users')).order_by('-like_users__count')[:N]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

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

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def movie_likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if movie.like_users.filter(pk=request.user.pk).exists():
        # 좋아요 취소
        movie.like_users.remove(request.user)
        liked = False
    else:
        # 좋아요 누름
        movie.like_users.add(request.user)
        liked = True
    
    like_status = {
        'liked': liked,
        'count': movie.like_users.count(),
    }
    return JsonResponse(like_status)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_recommended(request):
    pass

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_search_list(request):
    query = request.GET.get('q')

    movies = Movie.objects.filter(title__icontains=query)
    paginator = Paginator(movies, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    serializer = MovieListSerializer(page_obj, many=True)
    return Response(serializer.data)



# Model 1: 
@api_view(['GET'])
def movie_recommended_model1(request):
    user = request.user
    user_reviews = Review.objects.filter(user=user)
    print(user)
    most_liked_genre = Movie.objects.filter(like_users__in=[user]).values('genre_ids').annotate(gcount=Count('id')).order_by('-gcount')[0]
    print(most_liked_genre)
    genre_serialized = SimpleGenreSeriliazer(Genre.objects.get(id=most_liked_genre['genre_ids']))

    movies = Movie.objects.exclude(like_users__in=[user]).exclude(reviews__in=user_reviews).filter(genre_ids__in=[most_liked_genre['genre_ids']])[:5]
    serializer = MovieListSerializer(movies, many=True)
    return JsonResponse({'genre': genre_serialized.data, 'recommendations': serializer.data})