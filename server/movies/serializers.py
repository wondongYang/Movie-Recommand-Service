from rest_framework import serializers
from .models import Movie
from community.models import Review
from django.contrib.auth import get_user_model

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path',)


class MovieSerializer(serializers.ModelSerializer):

    class ReviewSerilizer(serializers.ModelSerializer):

        class UserSerializer(serializers.ModelSerializer):

            class Meta:
                model = get_user_model()
                fields = ('username',)

        user = UserSerializer(read_only=True) 

        class Meta:
            model = Review
            fields = ('id','content', 'rank', 'user')
    
    title = serializers.CharField(min_length=1, max_length=100)
    reviews = ReviewSerilizer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre_ids', 'overview', 'release_date', 'poster_path', 'reviews')