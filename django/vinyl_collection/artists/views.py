from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Artist, Genre
from records.models import Album
from .forms import ArtistForm, GenreForm

# Create your views here.

def artist_list(request):
    """Display all artists with their albums"""
    artists = Artist.objects.prefetch_related('album_set').all()
    
    context = {
        'artists': artists,
        'total_artists': artists.count(),
        'total_albums': Album.objects.count(),
    }
    return render(request, 'artists/artist_list.html', context)

def artist_detail(request, pk):
    """Display single artist with their albums"""
    artist = get_object_or_404(
        Artist.objects.prefetch_related('album_set__genre'),
        pk=pk
    )
    
    # Get albums sorted by release year
    albums = artist.album_set.all().order_by('release_year')
    
    context = {
        'artist': artist,
        'albums': albums,
        'album_count': albums.count(),
    }
    return render(request, 'artists/artist_detail.html', context)

def artist_create_ajax(request):
    """Create new artist via AJAX for use in album creation"""
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return JsonResponse({
                'success': True,
                'artist_id': artist.id,
                'artist_name': artist.name,
                'message': f'Artist "{artist.name}" created successfully!'
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def genre_create_ajax(request):
    """Create new genre via AJAX for use in album creation"""
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save()
            return JsonResponse({
                'success': True,
                'genre_id': genre.id,
                'genre_name': genre.name,
                'message': f'Genre "{genre.name}" created successfully!'
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})
