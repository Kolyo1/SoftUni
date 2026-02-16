# artists/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Artist(models.Model):
    """Model representing a musician or band"""
    
    class FormationType(models.TextChoices):
        SOLO = 'Solo', 'Solo Artist'
        BAND = 'Band', 'Band/Group'
        DUO = 'Duo', 'Duo'
    
    name = models.CharField(
        max_length=200, 
        unique=True,
        verbose_name="Artist/Band Name",
        help_text="Enter the full artist or band name"
    )
    formation_type = models.CharField(
        max_length=10,
        choices=FormationType.choices,
        default=FormationType.SOLO,
        verbose_name="Type"
    )
    country = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Country of Origin"
    )
    formed_year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2026)],
        null=True,
        blank=True,
        verbose_name="Year Formed"
    )
    biography = models.TextField(
        blank=True,
        verbose_name="Biography"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    @property
    def album_count(self):
        return self.album_set.count()


class Genre(models.Model):
    """Music genres"""
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Genre Name"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Description"
    )
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name