from django import forms
from .models import Album, Track
from artists.models import Artist, Genre

class AlbumForm(forms.ModelForm):
    """Main form for adding/editing albums"""
    
    # Custom field with additional validation
    release_year = forms.IntegerField(
        min_value=1900,
        max_value=2026,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., 1973'
        }),
        error_messages={
            'min_value': 'Vinyl records didn\'t exist before 1900!',
            'max_value': 'Cannot add albums from the future!'
        }
    )
    
    class Meta:
        model = Album
        fields = ['title', 'artist', 'genre', 'release_year', 
                 'condition', 'speed', 'catalog_number', 'notes']
        # Exclude auto-generated fields like date_added, last_played
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter album title'
            }),
            'artist': forms.Select(attrs={
                'class': 'form-control'
            }),
            'genre': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'size': '5'
            }),
            'condition': forms.Select(attrs={
                'class': 'form-control'
            }),
            'speed': forms.Select(attrs={
                'class': 'form-control'
            }),
            'catalog_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., PC 1234'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Add any personal notes...'
            }),
        }
        
        labels = {
            'catalog_number': 'Catalog Number (Optional)',
            'notes': 'Personal Notes',
        }
        
        help_texts = {
            'genre': 'Hold Ctrl/Cmd to select multiple genres',
        }
    
    def clean_title(self):
        """Custom validation for title"""
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise forms.ValidationError("Album title must be at least 2 characters long!")
        return title.title()  # Auto-format title


class TrackForm(forms.ModelForm):
    """Form for adding tracks to an album"""
    
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
                'placeholder': 'HH:MM:SS',
                'type': 'time'
            }, format='%H:%M:%S'),
            'track_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1'
            }),
        }
    
    def clean_track_number(self):
        """Ensure track number is positive"""
        number = self.cleaned_data.get('track_number')
        if number and number < 1:
            raise forms.ValidationError("Track number must be 1 or greater")
        return number


class AlbumSearchForm(forms.Form):
    """Form for filtering/sorting albums (read-only fields demo)"""
    
    SEARCH_CHOICES = [
        ('title', 'Album Title'),
        ('artist', 'Artist Name'),
        ('year', 'Release Year'),
    ]
    
    SORT_CHOICES = [
        ('title', 'Title A-Z'),
        ('-title', 'Title Z-A'),
        ('release_year', 'Year (Oldest First)'),
        ('-release_year', 'Year (Newest First)'),
        ('artist__name', 'Artist A-Z'),
    ]
    
    search_query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search your collection...'
        })
    )
    
    search_by = forms.ChoiceField(
        choices=SEARCH_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        required=False,
        empty_label="All Genres",
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
        choices=SORT_CHOICES,
        required=False,
        initial='title',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Read-only field example
    total_records = forms.IntegerField(
        required=False,
        disabled=True,  # This makes it read-only
        widget=forms.NumberInput(attrs={
            'class': 'form-control bg-light',
            'readonly': True
        })
    )
    
    def __init__(self, *args, **kwargs):
        total = kwargs.pop('total_records', 0)
        super().__init__(*args, **kwargs)
        self.fields['total_records'].initial = total