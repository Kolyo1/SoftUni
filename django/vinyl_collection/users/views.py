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
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_albums'] = Album.objects.count()
        context['total_reviews'] = Review.objects.count()
        context['total_users'] = User.objects.count()
        context['latest_albums'] = Album.objects.select_related('artist').prefetch_related('genre')[:5]
        return context


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        messages.success(self.request, 'Registration successful! Please log in.')
        return response


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_albums'] = Album.objects.filter(owner=user)[:10]
        context['user_reviews'] = Review.objects.filter(author=user)
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile_form.html'
    success_url = reverse_lazy('profile_detail')

    def get_object(self):
        return self.request.user.profile

    def form_valid(self, form):
        user = self.request.user
        user.first_name = form.cleaned_data.get('first_name', '')
        user.last_name = form.cleaned_data.get('last_name', '')
        user.email = form.cleaned_data.get('email', '')
        user.save()
        messages.success(self.request, 'Profile updated successfully!')
        return super().form_valid(form)
