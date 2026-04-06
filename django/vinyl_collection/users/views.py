from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Profile
from .forms import UserRegistrationForm, ProfileForm
from records.models import Album
from reviews.models import Review


class HomeView(TemplateView):
    """Dashboard/home view"""
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_albums'] = Album.objects.count()
        context['total_reviews'] = Review.objects.count()
        context['total_users'] = User.objects.count()
        # Show latest albums
        context['latest_albums'] = Album.objects.select_related('artist').prefetch_related('genre')[:5]
        return context


class RegisterView(CreateView):
    """User registration view"""
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Create profile for new user
        Profile.objects.create(user=self.object)
        messages.success(self.request, 'Registration successful! Please log in.')
        return response


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """View user profile"""
    model = Profile
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_albums'] = Album.objects.filter(artist__isnull=False)[:10]  # Can be refined
        context['user_reviews'] = Review.objects.filter(author=user)
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Edit user profile"""
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile_form.html'
    success_url = reverse_lazy('profile_detail')

    def get_object(self):
        return self.request.user.profile

    def form_valid(self, form):
        # Update user fields
        user = self.request.user
        user.first_name = form.cleaned_data.get('first_name', '')
        user.last_name = form.cleaned_data.get('last_name', '')
        user.email = form.cleaned_data.get('email', '')
        user.save()
        messages.success(self.request, 'Profile updated successfully!')
        return super().form_valid(form)
