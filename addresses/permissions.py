from rest_framework import permissions
from .models import Address
from rest_framework.views import View


class IsAdmOrAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif isinstance(obj, Address):
            return obj.user == request.user
        else:
            return False
