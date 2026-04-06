from django.db import models
from django.contrib.auth.models import User
from records.models import Album
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    """User reviews for albums"""
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='album_reviews'
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Rating (1-5)"
    )
    title = models.CharField(
        max_length=200,
        verbose_name="Review Title"
    )
    content = models.TextField(
        verbose_name="Review Content"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['album', 'author']
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f"Review by {self.author.username} for {self.album.title}"
