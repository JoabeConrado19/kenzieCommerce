from rest_framework import permissions
from rest_framework.views import View, Request


class IsAdmOrSeller(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        if request.user.is_seller:
            return True