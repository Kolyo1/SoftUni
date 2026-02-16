# records/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from artists.models import Artist, Genre

class Album(models.Model):
    class Condition(models.TextChoices):
        MINT = 'Mint', 'Mint (Perfect)'
        NEAR_MINT = 'Near Mint', 'Near Mint'
        VERY_GOOD = 'Very Good', 'Very Good'
        GOOD = 'Good', 'Good'
        FAIR = 'Fair', 'Fair'
        POOR = 'Poor', 'Poor'
    

    
    class Speed(models.TextChoices):
        THIRTY_THREE = '33', '33 ⅓ RPM'
        FORTY_FIVE = '45', '45 RPM'
        SEVENTY_EIGHT = '78', '78 RPM'
    
    # Basic info
    title = models.CharField(
        max_length=200,
        verbose_name="Album Title"
    )
    artist = models.ForeignKey(
        Artist, 
        on_delete=models.CASCADE,
        verbose_name="Artist/Band"
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name="Genres"
    )
    
    # Physical details
    release_year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2026)],
        verbose_name="Release Year"
    )
    condition = models.CharField(
        max_length=20,
        choices=Condition.choices,
        default=Condition.GOOD,
        verbose_name="Vinyl Condition"
    )
    speed = models.CharField(
        max_length=10,
        choices=Speed.choices,
        default=Speed.THIRTY_THREE,
        verbose_name="Playback Speed"
    )
    
    # Additional info
    catalog_number = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Catalog Number"
    )
    notes = models.TextField(
        blank=True,
        verbose_name="Personal Notes"
    )
    
    # Auto fields
    date_added = models.DateField(auto_now_add=True)
    last_played = models.DateField(
        null=True, 
        blank=True,
        verbose_name="Last Played"
    )
    
    class Meta:
        ordering = ['artist__name', 'release_year']
    
    def __str__(self):
        return f"{self.title} - {self.artist.name} ({self.release_year})"
    
    @property
    def is_classic(self):
        """Check if album is over 30 years old"""
        from django.utils import timezone
        current_year = timezone.now().year
        return (current_year - self.release_year) >= 30


class Track(models.Model):
    album = models.ForeignKey(
        Album, 
        on_delete=models.CASCADE, 
        related_name='tracks'
    )
    title = models.CharField(max_length=200)
    duration = models.DurationField(
        help_text="Format: HH:MM:SS",
        null=True,  # Make it optional for now
        blank=True
    )
    track_number = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
    
    class Meta:
        ordering = ['track_number']
        unique_together = ['album', 'track_number']
    
    def __str__(self):
        return f"{self.track_number}. {self.title}"