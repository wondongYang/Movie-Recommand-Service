from rest_framework import serializers
from .models import Review, Comment
from movies.models import Movie
from django.contrib.auth import get_user_model


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'review')


# class ReviewListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ()



class ReviewSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title',)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username',)

    class CommentSerializer(serializers.ModelSerializer):
        class CommentUserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('id', 'username',)
        user = CommentUserSerializer(read_only=True)
        class Meta:
            model = Comment
            fields = ('id', 'content', 'user')

    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('like_users')