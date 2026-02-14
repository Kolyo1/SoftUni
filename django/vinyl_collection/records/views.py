from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Album, Track
from .forms import AlbumForm, TrackForm, AlbumSearchForm
from artists.models import Artist, Genre

def album_list(request):
    """Display all albums with filtering/sorting"""
    albums = Album.objects.select_related('artist').prefetch_related('genre').all()
    
    # Initialize search form with total count
    form = AlbumSearchForm(request.GET or None, total_records=albums.count())
    
    if form.is_valid():
        # Apply filters
        search_query = form.cleaned_data.get('search_query')
        search_by = form.cleaned_data.get('search_by')
        genre = form.cleaned_data.get('genre')
        conditions = form.cleaned_data.get('condition')
        sort_by = form.cleaned_data.get('sort_by')
        
        if search_query and search_by:
            if search_by == 'title':
                albums = albums.filter(title__icontains=search_query)
            elif search_by == 'artist':
                albums = albums.filter(artist__name__icontains=search_query)
            elif search_by == 'year':
                albums = albums.filter(release_year__icontains=search_query)
        
        if genre:
            albums = albums.filter(genre=genre)
        
        if conditions:
            albums = albums.filter(condition__in=conditions)
        
        if sort_by:
            albums = albums.order_by(sort_by)
    
    context = {
        'albums': albums,
        'form': form,
        'total_albums': albums.count(),
        'genres': Genre.objects.all(),
    }
    return render(request, 'records/album_list.html', context)

def album_detail(request, pk):
    """Display single album details"""
    album = get_object_or_404(
        Album.objects.select_related('artist').prefetch_related('genre', 'tracks'),
        pk=pk
    )
    
    # Get similar albums (same genre, different artist)
    similar_albums = Album.objects.filter(
        genre__in=album.genre.all()
    ).exclude(pk=pk).distinct()[:5]
    
    context = {
        'album': album,
        'similar_albums': similar_albums,
    }
    return render(request, 'records/album_detail.html', context)


def album_create(request):
    """Create new album with tracks"""
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        track_form = TrackForm(request.POST)
        
        if form.is_valid():
            album = form.save()
            
            # Handle tracks if provided
            if track_form.is_valid() and track_form.cleaned_data.get('title'):
                track = track_form.save(commit=False)
                track.album = album
                track.save()
                messages.success(request, f'Album "{album.title}" added successfully with track!')
            else:
                messages.success(request, f'Album "{album.title}" added successfully!')
            
            return redirect('album_detail', pk=album.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AlbumForm()
        track_form = TrackForm()
    
    context = {
        'form': form,
        'track_form': track_form,
        'title': 'Add New Album',
    }
    return render(request, 'records/album_form.html', context)


def album_update(request, pk):
    """Edit existing album"""
    album = get_object_or_404(Album, pk=pk)
    
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'Album "{album.title}" updated successfully!')
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    
    context = {
        'form': form,
        'album': album,
        'title': f'Edit: {album.title}',
    }
    return render(request, 'records/album_form.html', context)


def album_delete(request, pk):
    """Delete album with confirmation"""
    album = get_object_or_404(Album, pk=pk)
    
    if request.method == 'POST':
        album.delete()
        messages.success(request, f'Album "{album.title}" deleted successfully!')
        return redirect('album_list')
    
    context = {
        'album': album,
        'related_tracks': album.tracks.count(),
    }
    return render(request, 'records/album_confirm_delete.html', context)