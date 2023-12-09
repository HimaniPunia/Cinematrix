from rest_framework import serializers
from cinematrix_api.models import *

class MovieSerializer(serializers.ModelSerializers):
    class Meta:
        model = Movie
        fields = '__all__'

class UserSerializer(serializers.ModelSerializers):
    favourite_movie = MovieSerializer(many = True)
    class Meta:
        model = User
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    movie_language = serializers.RelatedField(source = 'movie')
    class Meta:
        model = Language
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    movie_genre = serializers.RelatedField(source='movie')
    class Meta:
        model = Genre
        fields = '__all__'

class StreamingSiteSerializer(serializers.ModelSerializer):
    movie_streaming_site = serializers.RelatedField(source='movie')
    class Meta:
        model = StreamingSite
        fields = '__all__'
