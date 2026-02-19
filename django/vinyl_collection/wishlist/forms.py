from django import forms
from .models import WishlistItem
from artists.models import Artist

class WishlistItemForm(forms.ModelForm):
    class Meta:
        model = WishlistItem
        fields = ['artist', 'temporary_artist', 'album_title', 'priority', 'max_price', 'notes', 'is_available']
        widgets = {
            'artist': forms.Select(attrs={'class': 'form-select'}),
            'temporary_artist': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter artist name if not in list'}),
            'album_title': forms.TextInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'max_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['artist'].empty_label = "-- Select Artist --"
        self.fields['artist'].required = False
        self.fields['temporary_artist'].required = False
        self.fields['notes'].required = False
        self.fields['max_price'].required = False
        self.fields['is_available'].label = "Mark as available for purchase"
    
    def clean(self):
        cleaned_data = super().clean()
        artist = cleaned_data.get('artist')
        temporary_artist = cleaned_data.get('temporary_artist')
        
        if not artist and not temporary_artist:
            raise forms.ValidationError("Please select an artist or enter a temporary artist name.")
        
        if artist and temporary_artist:
            raise forms.ValidationError("Please select either an existing artist or enter a temporary artist name, not both.")
        
        return cleaned_data