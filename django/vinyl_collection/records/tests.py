from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from artists.models import Artist, Genre
from records.models import Album, Track


class AlbumModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.artist = Artist.objects.create(
            name='Test Artist',
            formation_type='Solo',
            country='USA'
        )
        self.genre = Genre.objects.create(name='Rock')
        
    def test_album_creation(self):
        album = Album.objects.create(
            title='Test Album',
            artist=self.artist,
            release_year=2023,
            owner=self.user
        )
        album.genre.add(self.genre)
        
        self.assertEqual(album.title, 'Test Album')
        self.assertEqual(album.artist, self.artist)
        self.assertEqual(album.owner, self.user)
        self.assertIn(self.genre, album.genre.all())
        
    def test_album_str_method(self):
        album = Album.objects.create(
            title='Test Album',
            artist=self.artist,
            release_year=2023,
            owner=self.user
        )
        expected_str = 'Test Album - Test Artist (2023)'
        self.assertEqual(str(album), expected_str)
        
    def test_album_is_classic_property(self):
        old_album = Album.objects.create(
            title='Old Album',
            artist=self.artist,
            release_year=1990,
            owner=self.user
        )
        new_album = Album.objects.create(
            title='New Album',
            artist=self.artist,
            release_year=2023,
            owner=self.user
        )
        
        self.assertTrue(old_album.is_classic)
        self.assertFalse(new_album.is_classic)


class TrackModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.artist = Artist.objects.create(name='Test Artist')
        self.album = Album.objects.create(
            title='Test Album',
            artist=self.artist,
            release_year=2023,
            owner=self.user
        )
        
    def test_track_creation(self):
        track = Track.objects.create(
            album=self.album,
            title='Test Track',
            track_number=1
        )
        
        self.assertEqual(track.title, 'Test Track')
        self.assertEqual(track.album, self.album)
        self.assertEqual(track.track_number, 1)
        
    def test_track_str_method(self):
        track = Track.objects.create(
            album=self.album,
            title='Test Track',
            track_number=1
        )
        expected_str = '1. Test Track'
        self.assertEqual(str(track), expected_str)


class AlbumViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='otherpass123'
        )
        self.artist = Artist.objects.create(name='Test Artist')
        self.genre = Genre.objects.create(name='Rock')
        self.album = Album.objects.create(
            title='Test Album',
            artist=self.artist,
            release_year=2023,
            owner=self.user
        )
        self.album.genre.add(self.genre)
        
    def test_album_list_view_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('album_list'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Album')
        self.assertEqual(len(response.context['albums']), 1)
        
    def test_album_list_view_unauthenticated(self):
        response = self.client.get(reverse('album_list'))
        
        # Should redirect to login
        self.assertEqual(response.status_code, 302)
        
    def test_album_list_view_other_user(self):
        self.client.login(username='otheruser', password='otherpass123')
        response = self.client.get(reverse('album_list'))
        
        self.assertEqual(response.status_code, 200)
        # Should not show other user's albums
        self.assertEqual(len(response.context['albums']), 0)
        
    def test_album_detail_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('album_detail', kwargs={'pk': self.album.pk}))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Album')
        self.assertContains(response, 'Test Artist')
        
    def test_album_create_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('album_create'), {
            'title': 'New Album',
            'artist': self.artist.pk,
            'release_year': 2023,
            'condition': 'Good',
            'speed': '33',
            'genre': [self.genre.pk],
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Album.objects.filter(title='New Album').exists())
        new_album = Album.objects.get(title='New Album')
        self.assertEqual(new_album.owner, self.user)
        
    def test_album_update_view_owner(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('album_update', kwargs={'pk': self.album.pk}), {
            'title': 'Updated Album',
            'artist': self.artist.pk,
            'release_year': 2023,
            'condition': 'Good',
            'speed': '33',
            'genre': [self.genre.pk],
        })
        
        self.assertEqual(response.status_code, 302)
        self.album.refresh_from_db()
        self.assertEqual(self.album.title, 'Updated Album')
        
    def test_album_update_view_non_owner(self):
        self.client.login(username='otheruser', password='otherpass123')
        response = self.client.post(reverse('album_update', kwargs={'pk': self.album.pk}), {
            'title': 'Updated Album',
            'artist': self.artist.pk,
            'release_year': 2023,
            'condition': 'Good',
            'speed': '33',
            'genre': [self.genre.pk],
        })
        
        self.assertEqual(response.status_code, 403)
        
    def test_album_delete_view_owner(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('album_delete', kwargs={'pk': self.album.pk}))
        
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Album.objects.filter(pk=self.album.pk).exists())
        
    def test_album_delete_view_non_owner(self):
        self.client.login(username='otheruser', password='otherpass123')
        response = self.client.post(reverse('album_delete', kwargs={'pk': self.album.pk}))
        
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Album.objects.filter(pk=self.album.pk).exists())
