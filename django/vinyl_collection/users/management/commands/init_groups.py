from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from records.models import Album, Track
from artists.models import Artist, Genre
from wishlist.models import WishlistItem
from reviews.models import Review
from users.models import Profile


class Command(BaseCommand):
    help = 'Create user groups and assign permissions'

    def handle(self, *args, **options):
        # Create groups
        admin_group, created = Group.objects.get_or_create(name='Collection Admins')
        power_user_group, created = Group.objects.get_or_create(name='Power Users')
        regular_user_group, created = Group.objects.get_or_create(name='Regular Users')

        # Get content types
        album_ct = ContentType.objects.get_for_model(Album)
        track_ct = ContentType.objects.get_for_model(Track)
        artist_ct = ContentType.objects.get_for_model(Artist)
        genre_ct = ContentType.objects.get_for_model(Genre)
        wishlist_ct = ContentType.objects.get_for_model(WishlistItem)
        review_ct = ContentType.objects.get_for_model(Review)
        profile_ct = ContentType.objects.get_for_model(Profile)

        # Admin permissions - full access
        admin_permissions = Permission.objects.filter(
            content_type__in=[album_ct, track_ct, artist_ct, genre_ct, wishlist_ct, review_ct, profile_ct]
        )
        admin_group.permissions.set(admin_permissions)

        # Power User permissions - can add/edit but not delete
        power_user_permissions = Permission.objects.filter(
            content_type__in=[album_ct, track_ct, artist_ct, genre_ct, wishlist_ct, review_ct],
            codename__in=['add_album', 'change_album', 'add_track', 'change_track', 
                          'add_artist', 'change_artist', 'add_genre', 'change_genre',
                          'add_wishlistitem', 'change_wishlistitem', 'add_review', 'change_review',
                          'view_album', 'view_track', 'view_artist', 'view_genre', 
                          'view_wishlistitem', 'view_review']
        )
        power_user_group.permissions.set(power_user_permissions)

        # Regular User permissions - can only manage their own content
        regular_user_permissions = Permission.objects.filter(
            content_type__in=[album_ct, wishlist_ct, review_ct],
            codename__in=['add_album', 'change_album', 'add_wishlistitem', 'change_wishlistitem',
                          'add_review', 'change_review', 'view_album', 'view_wishlistitem', 'view_review']
        )
        regular_user_group.permissions.set(regular_user_permissions)

        self.stdout.write(
            self.style.SUCCESS('Successfully created groups and assigned permissions')
        )
