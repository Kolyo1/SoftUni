# wishlist/models.py
from django.db import models
from django.core.validators import MinValueValidator
from artists.models import Artist

class WishlistItem(models.Model):
    class Priority(models.TextChoices):
        LOW = 'Low', 'Low Priority'
        MEDIUM = 'Medium', 'Medium Priority'
        HIGH = 'High', 'High Priority'
        URGENT = 'Urgent', 'Urgent - Must Have!'
    
    artist = models.ForeignKey(
        Artist,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    temporary_artist = models.CharField(
        max_length=200,
        blank=True
    )
    album_title = models.CharField(max_length=200)
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    max_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0)]
    )
    notes = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    is_available = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-priority', 'album_title']
    
    def __str__(self):
        artist_name = self.artist.name if self.artist else self.temporary_artist
        return f"{self.album_title} - {artist_name}"