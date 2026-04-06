from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group


class GroupRequiredMixin(UserPassesTestMixin):
    """Mixin to require user to be in specific groups"""
    required_groups = []

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        
        if self.request.user.is_superuser:
            return True
            
        user_groups = self.request.user.groups.values_list('name', flat=True)
        return any(group in user_groups for group in self.required_groups)


class AdminRequiredMixin(GroupRequiredMixin):
    """Require admin group membership"""
    required_groups = ['Collection Admins']


class PowerUserRequiredMixin(GroupRequiredMixin):
    """Require power user or admin group membership"""
    required_groups = ['Collection Admins', 'Power Users']


class OwnerRequiredMixin:
    """Mixin to ensure user can only edit their own objects"""
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.owner == self.request.user and not self.request.user.is_superuser:
            # Check if user has admin permissions
            if not self.request.user.groups.filter(name='Collection Admins').exists():
                raise PermissionDenied("You don't have permission to edit this item.")
        return obj
