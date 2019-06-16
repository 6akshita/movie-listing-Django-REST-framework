from rest_framework import serializers
from .models import Movie, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializers(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields =('popularity', 'director', 'genre', 'imdb_score', 'name')

