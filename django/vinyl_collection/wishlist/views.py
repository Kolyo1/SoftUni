from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import WishlistItem
from .forms import WishlistItemForm
from records.models import Album
from artists.models import Artist, Genre

def wishlist_list(request):
    """Display all wishlist items"""
    wishlist_items = WishlistItem.objects.select_related('artist').all()
    
    context = {
        'wishlist_items': wishlist_items,
        'total_items': wishlist_items.count(),
    }
    return render(request, 'wishlist/wishlist_list.html', context)

def wishlist_create(request):
    """Add new item to wishlist"""
    if request.method == 'POST':
        form = WishlistItemForm(request.POST)
        if form.is_valid():
            wishlist_item = form.save()
            messages.success(request, f'"{wishlist_item.album_title}" added to wishlist!')
            return redirect('wishlist_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = WishlistItemForm()
    
    context = {
        'form': form,
        'title': 'Add to Wishlist',
    }
    return render(request, 'wishlist/wishlist_form.html', context)

def wishlist_delete(request, pk):
    """Remove item from wishlist"""
    wishlist_item = get_object_or_404(WishlistItem, pk=pk)
    
    if request.method == 'POST':
        album_title = wishlist_item.album_title
        wishlist_item.delete()
        messages.success(request, f'"{album_title}" removed from wishlist!')
        return redirect('wishlist_list')
    
    context = {
        'wishlist_item': wishlist_item,
    }
    return render(request, 'wishlist/wishlist_confirm_delete.html', context)

def move_to_collection(request, pk):
    """Move wishlist item to collection as a new album"""
    wishlist_item = get_object_or_404(WishlistItem, pk=pk)
    
    if request.method == 'POST':
        try:
            # Handle artist selection
            artist = wishlist_item.artist
            if not artist and wishlist_item.temporary_artist:
                # Create new artist from temporary name
                artist = Artist.objects.create(name=wishlist_item.temporary_artist)
            
            if not artist:
                messages.error(request, 'No artist specified. Please select or create an artist first.')
                return redirect('wishlist_list')
            
            # Create new album from wishlist item
            album = Album.objects.create(
                title=wishlist_item.album_title,
                artist=artist,
                release_year=2024,  # Default year, can be updated later
                condition='Good',    # Default condition
            )
            
            # Add default genre if available
            default_genre = Genre.objects.first()
            if default_genre:
                album.genre.add(default_genre)
            
            # Store album title for message before deleting wishlist item
            album_title = wishlist_item.album_title
            
            # Remove from wishlist
            wishlist_item.delete()
            
            messages.success(
                request, 
                f'Great! "{album_title}" has been moved to your collection. '
                f'You can now edit the details to add release year, condition, and tracks.'
            )
            return redirect('album_detail', pk=album.pk)
            
        except Exception as e:
            messages.error(request, f'Error moving to collection: {str(e)}')
            return redirect('wishlist_list')
    
    context = {
        'wishlist_item': wishlist_item,
    }
    return render(request, 'wishlist/move_to_collection.html', context)
