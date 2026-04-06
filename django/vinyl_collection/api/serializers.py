from rest_framework import serializers
from records.models import Album, Track
from artists.models import Artist, Genre
from reviews.models import Review
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']


class ArtistSerializer(serializers.ModelSerializer):
    """Serializer for Artist model"""
    class Meta:
        model = Artist
        fields = ['id', 'name', 'country', 'formed_year', 'formation_type']
        read_only_fields = ['id']


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for Genre model"""
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']


class TrackSerializer(serializers.ModelSerializer):
    """Serializer for Track model"""
    class Meta:
        model = Track
        fields = ['id', 'title', 'track_number', 'duration']
        read_only_fields = ['id']


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review model"""
    author = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'rating', 'title', 'content', 'author', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'author']


class AlbumDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for Album with nested relationships"""
    artist = ArtistSerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    tracks = TrackSerializer(many=True, read_only=True, source='tracks')
    reviews = ReviewSerializer(many=True, read_only=True)
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        write_only=True,
        source='artist'
    )
    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        write_only=True,
        source='genre'
    )

    class Meta:
        model = Album
        fields = [
            'id', 'title', 'artist', 'artist_id', 'genre', 'genre_ids',
            'release_year', 'condition', 'speed', 'catalog_number',
            'notes', 'date_added', 'last_played', 'tracks', 'reviews'
        ]
        read_only_fields = ['id', 'date_added']


class AlbumListSerializer(serializers.ModelSerializer):
    """List serializer for Album (lighter version)"""
    artist = ArtistSerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = [
            'id', 'title', 'artist', 'genre', 'release_year',
            'condition', 'speed', 'date_added'
        ]
        read_only_fields = ['id', 'date_added']
