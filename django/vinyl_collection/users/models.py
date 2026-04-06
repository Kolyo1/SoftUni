from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """User profile extending the built-in User model"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(
        blank=True,
        verbose_name="Biography"
    )
    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        null=True,
        blank=True,
        verbose_name="Profile Photo"
    )
    website = models.URLField(
        blank=True,
        verbose_name="Website"
    )
    location = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Location"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return f"Profile of {self.user.username}"

    def get_full_name(self):
        """Get user's full name"""
        return f"{self.user.first_name} {self.user.last_name}".strip() or self.user.username
