from rest_framework import serializers
from .models import Movie
from community.models import Review

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', )


class MovieSerializer(serializers.ModelSerializer):

    class ReviewSerilizer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('id', 'title',)
    
    title = serializers.CharField(min_length=1, max_length=100)
    reviews = ReviewSerilizer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre_ids', 'overview', 'release_date', 'reviews', 'poster_path',)