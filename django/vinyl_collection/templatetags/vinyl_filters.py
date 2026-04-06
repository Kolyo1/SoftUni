from django import template
from django.utils import timezone
import re

register = template.Library()


@register.filter
def days_since(date):
    if not date:
        return "Never"
    
    delta = timezone.now().date() - date
    if delta.days == 0:
        return "Today"
    elif delta.days == 1:
        return "Yesterday"
    elif delta.days < 7:
        return f"{delta.days} days ago"
    elif delta.days < 30:
        weeks = delta.days // 7
        return f"{weeks} week{'s' if weeks != 1 else ''} ago"
    elif delta.days < 365:
        months = delta.days // 30
        return f"{months} month{'s' if months != 1 else ''} ago"
    else:
        years = delta.days // 365
        return f"{years} year{'s' if years != 1 else ''} ago"


@register.filter
def condition_class(condition):
    classes = {
        'Mint': 'success',
        'Near Mint': 'info',
        'Very Good': 'primary',
        'Good': 'warning',
        'Fair': 'secondary',
        'Poor': 'danger'
    }
    return classes.get(condition, 'secondary')


@register.filter
def priority_class(priority):
    classes = {
        'Urgent': 'danger',
        'High': 'warning',
        'Medium': 'info',
        'Low': 'secondary'
    }
    return classes.get(priority, 'secondary')


@register.filter
def rating_stars(rating):
    if not rating:
        return ""
    
    full_stars = '★' * rating
    empty_stars = '☆' * (5 - rating)
    return full_stars + empty_stars


@register.filter
def truncate_words(text, num_words):
    if not text:
        return ""
    
    words = text.split()
    if len(words) <= num_words:
        return text
    
    return ' '.join(words[:num_words]) + '...'


@register.filter
def format_duration(duration):
    if not duration:
        return ""
    
    total_seconds = duration.total_seconds()
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    
    if minutes > 0:
        return f"{minutes}:{seconds:02d}"
    else:
        return f"0:{seconds:02d}"


@register.filter
def currency(value):
    try:
        return f"${float(value):.2f}"
    except (ValueError, TypeError):
        return "$0.00"


@register.simple_tag
def collection_stats(user):
    if not user or not user.is_authenticated:
        return {}
    
    from records.models import Album
    from wishlist.models import WishlistItem
    from reviews.models import Review
    
    albums = Album.objects.filter(owner=user)
    wishlist_items = WishlistItem.objects.filter(owner=user)
    reviews = Review.objects.filter(author=user)
    
    return {
        'total_albums': albums.count(),
        'total_artists': albums.values('artist').distinct().count(),
        'wishlist_count': wishlist_items.count(),
        'urgent_wishlist': wishlist_items.filter(priority='Urgent').count(),
        'available_wishlist': wishlist_items.filter(is_available=True).count(),
        'total_reviews': reviews.count(),
    }
