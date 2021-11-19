from rest_framework import serializers
from .models import Review, Comment
from movies.models import Movie
from django.contrib.auth import get_user_model


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'review')


class ReviewSerializer(serializers.ModelSerializer):

    class MovieSerilizer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('id', 'title',)

    class UserSerializer(serializers.ModelSerializer):

            class Meta:
                model = get_user_model()
                fields = ('username',)

    user = UserSerializer(read_only=True) 
    movies = MovieSerilizer(many=True, read_only=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movies', 'user')
