from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def condition_badge(condition):
    """Convert condition to colored badge"""
    colors = {
        'Mint': 'success',
        'Near Mint': 'info',
        'Very Good': 'primary',
        'Good': 'warning',
        'Fair': 'danger',
        'Poor': 'dark',
    }
    color = colors.get(condition, 'secondary')
    return mark_safe(f'<span class="badge bg-{color}">{condition}</span>')


@register.filter
def format_duration(duration):
    """Format duration from timedelta to MM:SS"""
    if not duration:
        return "00:00"
    total_seconds = int(duration.total_seconds())
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"


@register.simple_tag
def total_albums():
    """Get total album count"""
    from records.models import Album
    return Album.objects.count()


@register.simple_tag
def total_artists():
    """Get total artist count"""
    from artists.models import Artist
    return Artist.objects.count()


@register.inclusion_tag('records/partials/album_card.html')
def album_card(album):
    """Reusable album card template"""
    return {'album': album}