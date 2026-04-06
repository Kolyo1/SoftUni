from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Album, Track
from artists.models import Artist, Genre


class AlbumForm(forms.ModelForm):
    release_year = forms.IntegerField(
        min_value=1900,
        max_value=timezone.now().year + 1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., 1973'
        }),
        error_messages={
            'min_value': 'Release year must be 1900 or later',
            'max_value': 'Release year cannot be in the future'
        }
    )
    
    class Meta:
        model = Album
        fields = ['title', 'artist', 'genre', 'release_year', 
                 'condition', 'speed', 'catalog_number', 'notes']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Album title'
            }),
            'artist': forms.Select(attrs={
                'class': 'form-control'
            }),
            'genre': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'size': '4'
            }),
            'condition': forms.Select(attrs={
                'class': 'form-control'
            }),
            'speed': forms.Select(attrs={
                'class': 'form-control'
            }),
            'catalog_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Catalog number (optional)'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Personal notes about this album'
            }),
        }
        
        help_texts = {
            'genre': 'Select multiple genres by holding Ctrl/Cmd',
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if len(title) < 2:
            raise forms.ValidationError("Album title must be at least 2 characters long")
        return title
    
    def clean_catalog_number(self):
        catalog = self.cleaned_data.get('catalog_number', '').strip()
        if catalog:
            catalog = catalog.upper()
            if len(catalog) > 30:
                raise forms.ValidationError("Catalog number is too long")
        return catalog
    
    def clean(self):
        cleaned_data = super().clean()
        release_year = cleaned_data.get('release_year')
        condition = cleaned_data.get('condition')
        
        if release_year and condition:
            age = timezone.now().year - release_year
            if age > 40 and condition == 'Mint':
                raise ValidationError({
                    'condition': 'Albums over 40 years old are unlikely to be in mint condition'
                })
        
        return cleaned_data


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'duration', 'track_number']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Track title'
            }),
            'duration': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
            'track_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1'
            }),
        }
    
    def clean_track_number(self):
        number = self.cleaned_data.get('track_number')
        if number and number < 1:
            raise forms.ValidationError("Track number must be at least 1")
        return number


class AlbumSearchForm(forms.Form):
    search_query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search albums...'
        })
    )
    
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        required=False,
        empty_label="All genres",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    condition = forms.MultipleChoiceField(
        choices=Album.Condition.choices,
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control',
            'size': '3'
        })
    )
    
    sort_by = forms.ChoiceField(
        choices=[
            ('title', 'Title A-Z'),
            ('-title', 'Title Z-A'),
            ('release_year', 'Year (oldest first)'),
            ('-release_year', 'Year (newest first)'),
        ],
        required=False,
        initial='title',
        widget=forms.Select(attrs={'class': 'form-control'})
    )