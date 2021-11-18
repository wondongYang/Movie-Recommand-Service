from rest_framework import serializers
from .models import Review, Comment
from movies.models import Movie


class ReviewSerializer(serializers.ModelSerializer):

    class MovieSerilizer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title',)
    
    movies = MovieSerilizer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movies',)

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'