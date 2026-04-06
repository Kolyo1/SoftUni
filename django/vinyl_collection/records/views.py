from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from .models import Album, Track
from .forms import AlbumForm, TrackForm, AlbumSearchForm
from artists.models import Artist, Genre


class AlbumListView(ListView):
    """Display all albums with filtering/sorting"""
    model = Album
    template_name = 'records/album_list.html'
    context_object_name = 'albums'
    paginate_by = 20

    def get_queryset(self):
        albums = Album.objects.select_related('artist').prefetch_related('genre').all()
        
        # Apply filtering
        search_query = self.request.GET.get('search_query', '')
        search_by = self.request.GET.get('search_by', '')
        genre_id = self.request.GET.get('genre', '')
        conditions = self.request.GET.getlist('condition')
        sort_by = self.request.GET.get('sort_by', 'title')
        
        if search_query and search_by:
            if search_by == 'title':
                albums = albums.filter(title__icontains=search_query)
            elif search_by == 'artist':
                albums = albums.filter(artist__name__icontains=search_query)
            elif search_by == 'year':
                albums = albums.filter(release_year__icontains=search_query)
        
        if genre_id:
            albums = albums.filter(genre=genre_id)
        
        if conditions:
            albums = albums.filter(condition__in=conditions)
        
        albums = albums.order_by(sort_by)
        return albums

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AlbumSearchForm(self.request.GET or None, total_records=self.get_queryset().count())
        context['genres'] = Genre.objects.all()
        context['total_albums'] = self.get_queryset().count()
        return context


class AlbumDetailView(DetailView):
    """Display single album details"""
    model = Album
    template_name = 'records/album_detail.html'
    context_object_name = 'album'
    queryset = Album.objects.select_related('artist').prefetch_related('genre', 'tracks', 'reviews')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.get_object()
        # Get similar albums (same genre, different artist)
        similar_albums = Album.objects.filter(
            genre__in=album.genre.all()
        ).exclude(pk=album.pk).distinct()[:5]
        context['similar_albums'] = similar_albums
        return context


class AlbumCreateView(LoginRequiredMixin, CreateView):
    """Create new album"""
    model = Album
    form_class = AlbumForm
    template_name = 'records/album_form.html'
    success_url = reverse_lazy('album_list')

    def form_valid(self, form):
        messages.success(self.request, f'Album "{form.cleaned_data["title"]}" added successfully!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Album'
        return context


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    """Edit existing album"""
    model = Album
    form_class = AlbumForm
    template_name = 'records/album_form.html'

    def form_valid(self, form):
        messages.success(self.request, f'Album "{form.cleaned_data["title"]}" updated successfully!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Edit: {self.get_object().title}'
        return context

    def get_success_url(self):
        return reverse_lazy('album_detail', kwargs={'pk': self.object.pk})


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    """Delete album with confirmation"""
    model = Album
    template_name = 'records/album_confirm_delete.html'
    success_url = reverse_lazy('album_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_tracks'] = self.get_object().tracks.count()
        return context

    def delete(self, request, *args, **kwargs):
        album_title = self.get_object().title
        messages.success(request, f'Album "{album_title}" deleted successfully!')
        return super().delete(request, *args, **kwargs)
