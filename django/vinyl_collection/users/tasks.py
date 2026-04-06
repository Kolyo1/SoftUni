from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from .models import Profile


@shared_task
def cleanup_old_notifications():
    """Clean up old user data and send maintenance notifications"""
    users_cleaned = 0
    
    # Find inactive users (no login for 6 months)
    six_months_ago = timezone.now() - timedelta(days=180)
    inactive_users = User.objects.filter(last_login__lt=six_months_ago)
    
    for user in inactive_users:
        # Send re-engagement email
        if user.email:
            send_re_engagement_email.delay(user.id)
            users_cleaned += 1
    
    return f"Processed {users_cleaned} inactive users"


@shared_task
def send_re_engagement_email(user_id):
    """Send re-engagement email to inactive users"""
    try:
        user = User.objects.get(id=user_id)
        
        subject = "We miss you at Vinyl Collection! 🎵"
        
        message = f"""
Hi {user.get_full_name() or user.username},

It's been a while since you last visited your vinyl collection!

Your collection is waiting for you:
• Add new albums you've acquired
• Update your wishlist with new finds
• Share your thoughts with reviews

We've also added some exciting new features:
• Daily collection statistics
• Wishlist availability notifications
• Enhanced search and filtering

Come back and continue building your amazing vinyl collection!

Login here: {settings.SITE_URL}/login/

If you need any help, just reply to this email.

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
        
        return f"Re-engagement email sent to {user.email}"
        
    except User.DoesNotExist:
        return f"User with ID {user_id} not found"
    except Exception as e:
        return f"Error sending re-engagement email: {str(e)}"


@shared_task
def generate_user_activity_report():
    """Generate weekly activity report for admins"""
    total_users = User.objects.count()
    active_users = User.objects.filter(
        last_login__gte=timezone.now() - timedelta(days=7)
    ).count()
    new_users = User.objects.filter(
        date_joined__gte=timezone.now() - timedelta(days=7)
    ).count()
    
    report = f"""
Weekly User Activity Report:
• Total Users: {total_users}
• Active Users (last 7 days): {active_users}
• New Users (last 7 days): {new_users}
• Activity Rate: {(active_users/total_users*100):.1f}%
    """
    
    # Send to admin users
    admin_users = User.objects.filter(is_superuser=True)
    for admin in admin_users:
        if admin.email:
            send_mail(
                "Weekly User Activity Report",
                report,
                settings.DEFAULT_FROM_EMAIL,
                [admin.email],
                fail_silently=False,
            )
    
    return f"Activity report sent to {admin_users.count()} admins"


@shared_task
def update_user_statistics():
    """Update user profile statistics"""
    users_updated = 0
    
    for user in User.objects.all():
        try:
            profile = user.profile
            
            # Update collection stats (could be stored in profile)
            # This is a placeholder for more complex statistics
            
            users_updated += 1
            
        except Profile.DoesNotExist:
            # Create profile if it doesn't exist
            Profile.objects.create(user=user)
            users_updated += 1
    
    return f"Updated statistics for {users_updated} users"
