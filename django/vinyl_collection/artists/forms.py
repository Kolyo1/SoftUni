from django import forms
from .models import Artist, Genre

class ArtistForm(forms.ModelForm):
    """Form for creating new artists"""
    
    class Meta:
        model = Artist
        fields = ['name', 'formation_type', 'country', 'formed_year', 'biography']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter artist or band name'
            }),
            'formation_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., United States, United Kingdom'
            }),
            'formed_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., 1960',
                'min': '1900',
                'max': '2026'
            }),
            'biography': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Add a brief biography or notes about this artist...'
            }),
        }
        
        labels = {
            'formed_year': 'Year Formed (Optional)',
            'biography': 'Biography (Optional)',
            'country': 'Country of Origin (Optional)',
        }
    
    def clean_name(self):
        """Custom validation for artist name"""
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError("Artist name must be at least 2 characters long!")
        
        # Check for duplicate artist names
        if Artist.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("An artist with this name already exists!")
        
        return name.strip()


class GenreForm(forms.ModelForm):
    """Form for creating new genres"""
    
    class Meta:
        model = Genre
        fields = ['name', 'description']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter genre name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Brief description of the genre...'
            }),
        }
    
    def clean_name(self):
        """Custom validation for genre name"""
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError("Genre name must be at least 2 characters long!")
        
        # Check for duplicate genre names
        if Genre.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("A genre with this name already exists!")
        
        return name.strip().title()  # Auto-format genre name