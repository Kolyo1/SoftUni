from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from django.urls import reverse
from users.models import Profile


class UserRegistrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_user_registration_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'password1': 'complexpass123',
            'password2': 'complexpass123'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        
        # Check that profile was created
        user = User.objects.get(username='newuser')
        self.assertTrue(Profile.objects.filter(user=user).exists())
        
    def test_user_registration_email_unique(self):
        User.objects.create_user(
            username='existinguser',
            email='test@example.com',
            password='testpass123'
        )
        
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'test@example.com',  # Same email
            'first_name': 'New',
            'last_name': 'User',
            'password1': 'complexpass123',
            'password2': 'complexpass123'
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'email', 'This email is already registered!')


class ProfileTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            bio='Test bio',
            location='Test City',
            website='https://example.com'
        )
        
    def test_profile_detail_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('profile_detail'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test User')
        self.assertContains(response, 'Test bio')
        
    def test_profile_update_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('profile_edit'), {
            'bio': 'Updated bio',
            'location': 'Updated City',
            'website': 'https://updated.com',
            'first_name': 'Updated',
            'last_name': 'Name',
            'email': 'updated@example.com'
        })
        
        self.assertEqual(response.status_code, 302)
        self.profile.refresh_from_db()
        self.user.refresh_from_db()
        
        self.assertEqual(self.profile.bio, 'Updated bio')
        self.assertEqual(self.user.first_name, 'Updated')
        self.assertEqual(self.user.email, 'updated@example.com')
        
    def test_profile_get_full_name(self):
        self.assertEqual(self.profile.get_full_name(), 'Test User')
        
        # Test with empty name
        self.user.first_name = ''
        self.user.last_name = ''
        self.user.save()
        self.assertEqual(self.profile.get_full_name(), 'testuser')


class LoginLogoutTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        Profile.objects.create(user=self.user)
        
    def test_login_view(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        
        self.assertEqual(response.status_code, 302)
        
    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('logout'))
        
        self.assertEqual(response.status_code, 302)
