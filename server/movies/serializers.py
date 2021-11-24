from rest_framework import serializers

# from server.accounts.serializers import UserSerializer
from .models import Genre, Movie
from community.models import Review
from django.contrib.auth import get_user, get_user_model

class MovieListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', )

    class ReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = ('id', 'content', 'rank', 'user')
    
    reviews = ReviewSerializer(many=True, read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        depth = 1


class MovieSerializer(serializers.ModelSerializer):

    class ReviewSerializer(serializers.ModelSerializer):
        
        class UserSerializer(serializers.ModelSerializer):

            class Meta:
                model = get_user_model()
                fields = ('id', 'username',)

        user = UserSerializer(read_only=True)
        
        class Meta:
            model = Review
            # fields = '__all__'
            fields = ('id', 'content', 'rank', 'user')
            
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        # fields = ('id', 'title', 'genre_ids', 'overview', 'release_date', 'poster_path', 'reviews')
        fields = '__all__'
        depth = 1

class SimpleGenreSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'