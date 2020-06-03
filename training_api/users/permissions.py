from rest_framework.permissions import SAFE_METHODS, BasePermission
from django.contrib.auth.models import AnonymousUser


class OwnUser(BasePermission):
    def has_permission(self, request, view):
        return view.action in ["update", "partial_update", "destroy"]

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class NewUser(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, AnonymousUser)

    def has_object_permission(self, request, view, obj):
        return False
