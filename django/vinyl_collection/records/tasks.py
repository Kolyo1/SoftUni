from celery import shared_task
from django.contrib.auth.models import User
from django.db.models import Count, Avg
from django.core.mail import send_mail
from django.conf import settings
from .models import Album
from artists.models import Artist, Genre
from wishlist.models import WishlistItem
from reviews.models import Review


@shared_task
def generate_collection_statistics():
    users = User.objects.all()
    
    for user in users:
        albums = Album.objects.filter(owner=user)
        wishlist_items = WishlistItem.objects.filter(owner=user)
        reviews = Review.objects.filter(author=user)
        
        stats = {
            'total_albums': albums.count(),
            'total_artists': albums.values('artist').distinct().count(),
            'wishlist_count': wishlist_items.count(),
            'urgent_items': wishlist_items.filter(priority='Urgent').count(),
        }
        
        if user.email and stats['total_albums'] > 0:
            send_collection_summary_email.delay(user.id, stats)
    
    return f"Generated statistics for {users.count()} users"


@shared_task
def send_collection_summary_email(user_id, stats):
    try:
        user = User.objects.get(id=user_id)
        
        subject = f"Your Vinyl Collection Summary"
        
        message = f"""
Hi {user.get_full_name() or user.username},

Here's your collection summary:

📊 Collection Overview:
• Total Albums: {stats['total_albums']}
• Total Artists: {stats['total_artists']}
• Wishlist Items: {stats['wishlist_count']}
• Urgent Items: {stats['urgent_items']}

Keep building your amazing collection!

Best regards,
Vinyl Collection Team
        """
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        
        return f"Email sent to {user.email}"
        
    except User.DoesNotExist:
        return f"User {user_id} not found"
    except Exception as e:
        return f"Error sending email: {str(e)}"
