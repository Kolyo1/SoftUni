from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import WishlistItem


@shared_task
def update_wishlist_availability():
    """Simulate updating wishlist availability (in real app, this would check external APIs)"""
    items_updated = 0
    
    # Simulate checking availability for wishlist items
    # In a real application, this would integrate with external APIs like Discogs
    wishlist_items = WishlistItem.objects.filter(is_available=False)
    
    for item in wishlist_items:
        # Simulate random availability check (10% chance of becoming available)
        import random
        if random.random() < 0.1:  # 10% chance
            item.is_available = True
            item.save()
            items_updated += 1
            
            # Notify user about availability
            send_availability_notification.delay(item.owner.id, item.id)
    
    return f"Updated availability for {items_updated} wishlist items"


@shared_task
def send_availability_notification(user_id, wishlist_item_id):
    """Send notification when wishlist item becomes available"""
    try:
        user = User.objects.get(id=user_id)
        item = WishlistItem.objects.get(id=wishlist_item_id)
        
        subject = f"🎵 '{item.album_title}' is now available!"
        
        message = f"""
Hi {user.get_full_name() or user.username},

Great news! An item from your wishlist is now available:

📀 {item.album_title}
🎤 {item.artist.name if item.artist else item.temporary_artist}
⭐ Priority: {item.get_priority_display()}
💰 Max Price: ${item.max_price if item.max_price else 'Not set'}

You can now add this to your collection or mark it as purchased.

Visit your wishlist to take action: {settings.SITE_URL}/wishlist/

Happy collecting!

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
        
        return f"Availability notification sent to {user.email} for '{item.album_title}'"
        
    except User.DoesNotExist:
        return f"User with ID {user_id} not found"
    except WishlistItem.DoesNotExist:
        return f"Wishlist item with ID {wishlist_item_id} not found"
    except Exception as e:
        return f"Error sending availability notification: {str(e)}"


@shared_task
def send_wishlist_reminder():
    """Send weekly reminder for high-priority wishlist items"""
    users = User.objects.all()
    reminders_sent = 0
    
    for user in users:
        # Get urgent and high priority items that aren't available
        priority_items = WishlistItem.objects.filter(
            owner=user,
            is_available=False
        ).filter(
            priority__in=['Urgent', 'High']
        )
        
        if priority_items.exists() and user.email:
            send_wishlist_summary_email.delay(user.id, list(priority_items.values()))
            reminders_sent += 1
    
    return f"Sent wishlist reminders to {reminders_sent} users"


@shared_task
def send_wishlist_summary_email(user_id, items):
    """Send weekly wishlist summary for priority items"""
    try:
        user = User.objects.get(id=user_id)
        
        subject = f"🎯 Your Priority Wishlist Items ({len(items)} items)"
        
        items_list = "\n".join([
            f"• {item['album_title']} - {item['priority']} priority"
            for item in items
        ])
        
        message = f"""
Hi {user.get_full_name() or user.username},

Here's a reminder of your high-priority wishlist items:

{items_list}

These are the items you marked as urgent or high priority. 
Keep an eye out for them to complete your collection!

Visit your wishlist: {settings.SITE_URL}/wishlist/

Happy hunting!

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
        
        return f"Wishlist summary sent to {user.email}"
        
    except User.DoesNotExist:
        return f"User with ID {user_id} not found"
    except Exception as e:
        return f"Error sending wishlist summary: {str(e)}"
