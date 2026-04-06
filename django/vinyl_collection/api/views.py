from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from records.models import Album, Track
from reviews.models import Review
from artists.models import Artist
from .serializers import (
    AlbumListSerializer, AlbumDetailSerializer, TrackSerializer,
    ReviewSerializer, ArtistSerializer
)


class AlbumViewSet(viewsets.ModelViewSet):
    """API ViewSet for Album CRUD operations"""
    queryset = Album.objects.select_related('artist').prefetch_related('genre', 'tracks', 'reviews').all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['artist', 'release_year', 'condition']
    search_fields = ['title', 'artist__name']
    ordering_fields = ['title', 'release_year', 'date_added']
    ordering = ['-date_added']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AlbumDetailSerializer
        return AlbumListSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def add_review(self, request, pk=None):
        """Add a review to an album"""
        album = self.get_object()
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(album=album, author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        """Get all reviews for an album"""
        album = self.get_object()
        reviews = album.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ArtistViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API ViewSet for Artist"""
    queryset = Artist.objects.prefetch_related('album_set').all()
    serializer_class = ArtistSerializer
    search_fields = ['name', 'country']
    ordering_fields = ['name', 'formed_year']
    ordering = ['name']


class ReviewViewSet(viewsets.ModelViewSet):
    """API ViewSet for Review management"""
    queryset = Review.objects.select_related('author', 'album').all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering_fields = ['rating', 'created_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """Only authors can update their reviews"""
        if serializer.instance.author != self.request.user:
            return Response(
                {'detail': 'You can only update your own reviews.'},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer.save()
