from rest_framework import serializers
from django.contrib.auth import get_user_model

from community.models import Review
from movies.models import Movie

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password',)



# 프로필에서 쓰일 영화 정보를 정의하기 위한 Serializer입니다.
# (좋아요한 영화, 리뷰 영화 정보, ...)
class ProfileMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path')

class UserProfileSerializer(serializers.ModelSerializer):
    
    like_movies = ProfileMovieSerializer(many=True, read_only=True)
    class ProfileReviewSerializer(serializers.ModelSerializer):
        movie = ProfileMovieSerializer(read_only=True)
        class Meta:
            model = Review
            fields = ('id', 'rank', 'movie', 'content',)
    like_reviews = ProfileReviewSerializer(many=True, read_only=True)
    review_set = ProfileReviewSerializer(many=True, read_only=True)
    # class WrittenReviewSerializer(serializers.ModelSerializer):
    #     class WRmovieSerializer(serializers.ModelSerializer):
    #         class Meta:
    #             model = Movie
    #             fields = ('id', 'title')
    #     movie = WRmovieSerializer(read_only=True)
    #     class Meta:
    #         model = Review
    #         fields = ('id', 'rank', 'movie')
    #         # fields = ('id',)

    # review_set = WrittenReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'date_joined', 'like_movies', 'like_reviews', 'review_set','comment_set')
        depth = 1